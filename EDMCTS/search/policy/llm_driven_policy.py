"""Class for the coherence policy."""
import sys

from collections.abc import Callable

import numpy as np
from scipy.special import softmax
from sklearn.preprocessing import MinMaxScaler
from sklearn.exceptions import NotFittedError

sys.path.append("src")
from search.policy.reasoner_policy import ReasonerPolicy  # noqa:402


class LLMDrivenReasonerPolicy(ReasonerPolicy):
    """A polocy like the Reasoner policy, but it promotes more coherent prompts."""

    def __init__(
        self,
        temperature: float = 0.6,
        attribute_1_types: list[str] = None,
        attribute_2_types: list[str] = None,
        method_label_types: list[str] = None,
        try_oxides: bool = True,
    ):
        """Create the underlying ReasonerPolicy."""
        super().__init__(
            attribute_1_types,
            attribute_2_types,
            method_label_types,
            try_oxides,
        )
        self.temperature = temperature

    @classmethod
    @staticmethod
    def from_reasoner_policy(
        reasoner_policy: ReasonerPolicy, temperature: float = 0.6
    ) -> "LLMDrivenReasonerPolicy":
        """Construct a coherent policy from a reasoner poliy."""
        p = LLMDrivenReasonerPolicy()
        p.actions = reasoner_policy.actions.copy()
        p.init_weights()
        return p

    def get_actions(
        self, states: object
    ) -> tuple[list[Callable[object, object]], np.array]:
        """Return the actions along with their priors."""
        actions, priors = super().get_actions(
            states
        )  # get super class actions and priors
        new_priors = []
        for i, state in enumerate(states):
            prev_answer = state.answer

            prior_prompt = f"Consider the previous answer:\n{prev_answer}.\n\n"
            if state.reward < 0:
                prior_prompt += (
                    "These methods were very poor recommendations. "
                    "We should try to find alternative catalysts."
                )
            elif state.reward < 5:
                prior_prompt += (
                    "These methods were weakly active. "
                    "Let's see if slight modifications can improve their results."
                )
            elif state.reward > 5:
                prior_prompt += (
                    "These methods were very active."
                    "Let's see if we can improve these recommendations a little bit."
                )
            prior_prompt += f"The catalysts {state.reward}.\n\n"
            prior_prompt += (
                "Your task is to rate the following actions to produce a "
                "new prompt that an llm can use to recommend better catalysts.\n\n"
            )

            actions_statement = "The actions are:\n"
            for i, a in enumerate(actions):
                if priors[0][i] != 0:
                    actions_statement += (
                        f"- {a.message(s)}\n"  # punctuation is in a.message
                    )

            prior_prompt += actions_statement
            prior_prompt += (
                "\nReturn you ranking of the top 5 actions to take. "
                "Take a deep breath and let's think step by step."
            )

            return prior_prompt
            new_priors.append(priors[i])

        return actions, new_priors


_answer = """Here are the top-5 regulation methods for achieving atomic level dispersion of Cu single atoms on carbon supports (Cu/C) to enhance ethanol production:

1. **Support Modification with Carbon Nanotubes (CNTs):**
   - **Regulation Method:** Incorporation of Cu single atoms onto carbon nanotubes (CNTs).
   - **Scientific Explanation:** CNTs provide a high surface area and unique electronic properties that can stabilize Cu single atoms. The tubular structure of CNTs can effectively disperse Cu atoms, preventing agglomeration and maximizing catalytic sites.

2. **Temperature Programmed Reduction (TPR) of Cu/C:**
   - **Regulation Method:** Controlled reduction of Cu species on carbon supports under programmed temperature conditions.
   - **Scientific Explanation:** TPR allows for precise reduction of Cu species to single atoms or small clusters, ensuring uniform dispersion on the carbon support. This method optimizes the interaction between Cu and carbon, enhancing the catalyst's activity and selectivity towards ethanol.

3. **Surface Functionalization with Oxygen Groups:**
   - **Regulation Method:** Introduction of oxygen functional groups (e.g., -OH, -COOH) on the surface of Cu/C.
   - **Scientific Explanation:** Oxygen groups can anchor Cu single atoms via strong metal-support interactions (SMSI), stabilizing the dispersion of Cu atoms. These groups also modify the electronic properties of Cu, potentially improving its catalytic performance towards ethanol production.

4. **Doping with Promoters such as Zn or In:**
   - **Regulation Method:** Incorporation of dopant atoms (e.g., Zn, In) into Cu single atom catalysts supported on carbon.
   - **Scientific Explanation:** Dopants like Zn or In can alter the electronic structure and surface properties of Cu, enhancing its dispersion and activity. These promoters can stabilize Cu single atoms and improve the catalyst's efficiency in ethanol synthesis.

5. **Atomic Layer Deposition (ALD) of Oxide Layers:**
   - **Regulation Method:** Deposition of thin oxide layers (e.g., Al₂O₃) on Cu single atom catalysts supported on carbon.
   - **Scientific Explanation:** ALD enables precise control over the thickness and composition of oxide layers on Cu/C, which can stabilize Cu single atoms and prevent sintering. The oxide layers act as supports that enhance the dispersion and catalytic performance of Cu in ethanol production.

Now, let's structure these into a Python list as requested:

```python
final_answer = [
    "Support Modification with Carbon Nanotubes (CNTs)",
    "Temperature Programmed Reduction (TPR) of Cu/C",
    "Surface Functionalization with Oxygen Groups",
    "Doping with Promoters such as Zn or In",
    "Atomic Layer Deposition (ALD) of Oxide Layers"
]
```

This list `final_answer` contains the top-5 regulation methods for achieving atomic level dispersion of Cu single atoms on carbon supports (Cu/C) to optimize ethanol production."""


class TestState:
    reward = 7
    candidates = [
        "Support Modification with Carbon Nanotubes (CNTs)",
        "Temperature Programmed Reduction (TPR) of Cu/C",
        "Surface Functionalization with Oxygen Groups",
        "Doping with Promoters such as Zn or In",
        "Atomic Layer Deposition (ALD) of Oxide Layers"
    ]

    def __init__(
        self,
        answer: str = _answer,
        candidates: list[str] = None,
        method_label: str = "surface/interface modification",
        attribute1_list: list[str] = [],
        attribute2_list: list[str] = [],
    ):
        self.answer = answer
        self.method_label = method_label
        self.attribute1_list = [""]
        self.attribute2_list = [""]


if __name__ == "__main__":
    from llm.automate_prompts import get_initial_state_oc

    with open(
        "data/output/example_answers_for_analysis.txt",
        "r",
    ) as f:
        answers = f.read()

    answers = answers.replace('"', "").split("<>")

    with open("data/output/example_prior_prompts_for_analysis.txt", "w") as f:
        for ans in answers:
            s = TestState(answer=ans)
            p = LLMDrivenReasonerPolicy(0.4)
            prompt = p.get_actions([s])

            f.write(prompt)

            f.write(
                "\n"
                + "####################################################\n" * 10
                + "\n"
            )
