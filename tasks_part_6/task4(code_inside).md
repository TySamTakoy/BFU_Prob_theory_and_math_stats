# ЗАДАНИЕ №4

Перед вами маг, который утверждает что с вероятностью $90$% способен предугадать на какую сторону упадет монета. Как поставить эксперимент с этим магом, чтобы доказать либо опровергнуть факт его магической силы. Как должен будет выглядеть эксперимент, если маг будет утверждать, что он способен предугадывать сторону выпадения монеты с вероятностью $51$%?

# РЕШЕНИЕ

```
from scipy.stats import binomtest
import random as rnd

def analyze_experiment(correct_predictions, total_trials, claimed_probability):
    p_value = binomtest(correct_predictions, total_trials, p=claimed_probability, alternative='greater')
    return p_value

# Пример для 90%
correct_predictions_90 = 900
total_trials_90 = 1000
claimed_probability_90 = 0.9
p_value_90 = analyze_experiment(correct_predictions_90, total_trials_90, claimed_probability_90)
if (p_value_90.pvalue)*100 < 90:
  print(f"P-value для 90% вероятности: {p_value_90.pvalue:.4f} => Гипотеза опровергнута")
else:
  print(f"P-value для 90% вероятности: {p_value_90.pvalue:.4f} => Гипотеза подтверждена")

# Пример для 51%
correct_predictions_51 = 5100
total_trials_51 = 10000
claimed_probability_51 = 0.51
p_value_51 = analyze_experiment(correct_predictions_51, total_trials_51, claimed_probability_51)
if (p_value_51.pvalue)*100 < 51:
  print(f"P-value для 51% вероятности: {p_value_51.pvalue:.4f} => Гипотеза опровергнута")
else:
  print(f"P-value для 51% вероятности: {p_value_51.pvalue:.4f} => Гипотеза подтверждена")
```

`P-value для 90% вероятности: 0.5266 => Гипотеза опровергнута`

`P-value для 51% вероятности: 0.5040 => Гипотеза опровергнута`
