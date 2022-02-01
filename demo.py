ham_freq = {'Dear': 8, 'Friend': 5, 'Lunch': 3, 'Money': 1}

spam_freq = {'Dear': 2, 'Friend': 1, 'Lunch': 0, 'Money': 4}

print('Probabilidades condicionais de não spams')
for word in ham_freq:
    p = ham_freq.get(word) / sum(ham_freq.values())
    print(p)

print('Probabilidades condicionais de spams')
for word in spam_freq:
    p = spam_freq.get(word) / sum(spam_freq.values())
    print(p)

prior_probability_ham = 8 / (8 + 4)
prior_probability_spam = 4 / (8 + 4)

example_email = ['Dear', 'Friend']


def calculate_proportional_probabilities(message):
    proportional_probability_ham = prior_probability_ham
    for word in message:
        proportional_probability_ham *= ham_freq.get(word) / sum(ham_freq.values())

    proportional_probability_spam = prior_probability_spam
    for word in message:
        proportional_probability_spam *= spam_freq.get(word) / sum(spam_freq.values())
    return proportional_probability_ham, proportional_probability_spam


proportional_probability_ham, proportional_probability_spam = calculate_proportional_probabilities(example_email)

print('Probabilidade de não ser spam dado a mensagem é proporcional a: ')
print(proportional_probability_ham)

print('Probabilidade de ser spam dado a mensagem é proporcional a: ')
print(proportional_probability_spam)

# Probabilidade de 0 em spam por causa de Lunch
example_email = ['Lunch', 'Money', 'Money', 'Money', 'Money']
print(calculate_proportional_probabilities(example_email))

# somar 1 nas frequencias
for word in ham_freq:
    ham_freq.update({word: ham_freq.get(word)+1})

for word in spam_freq:
    spam_freq.update({word: spam_freq.get(word)+1})
print(calculate_proportional_probabilities(['Dear', 'Friend']))
print(calculate_proportional_probabilities(example_email))

