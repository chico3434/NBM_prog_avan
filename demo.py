ham_freq = {'relatório': 7, 'reunião': 6, 'promoção': 2, 'desconto': 0}

spam_freq = {'relatório': 1, 'reunião': 1, 'promoção': 8, 'desconto': 5}

print('Probabilidades condicionais de não spams')
for word in ham_freq:
    p = ham_freq.get(word) / sum(ham_freq.values())
    print('P(H|{})={}'.format(word, p))

print('Probabilidades condicionais de spams')
for word in spam_freq:
    p = spam_freq.get(word) / sum(spam_freq.values())
    print('P(S|{})={}'.format(word, p))

prior_probability_ham = 8 / (8 + 8)
prior_probability_spam = 8 / (8 + 8)

example_email = ['relatório', 'reunião']


def calculate_proportional_probabilities(message):
    proportional_probability_ham = prior_probability_ham
    for word in message:
        proportional_probability_ham *= ham_freq.get(word) / sum(ham_freq.values())

    proportional_probability_spam = prior_probability_spam
    for word in message:
        proportional_probability_spam *= spam_freq.get(word) / sum(spam_freq.values())
    return proportional_probability_ham, proportional_probability_spam


def print_analise(message):
    proportional_probability_ham, proportional_probability_spam = calculate_proportional_probabilities(message)
    print(message)
    print('Probabilidade de não ser spam dado a mensagem é proporcional a: ')
    print(proportional_probability_ham)

    print('Probabilidade de ser spam dado a mensagem é proporcional a: ')
    print(proportional_probability_spam)
    if proportional_probability_ham > proportional_probability_spam:
        print('Provavelmente não é spam!')
    else:
        print('Provavelmente é spam!')


print_analise(example_email)

# Probabilidade de 0 em ham por causa de desconto
example_email = ['desconto', 'promoção', 'promoção', 'promoção', 'promoção']
print_analise(example_email)

# somar 1 nas frequencias
for word in ham_freq:
    ham_freq.update({word: ham_freq.get(word) + 1})

for word in spam_freq:
    spam_freq.update({word: spam_freq.get(word) + 1})
print_analise(['relatório', 'reunião'])
print_analise(example_email)
