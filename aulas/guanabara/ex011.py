# Programa para lear a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimesão de {} x {} e sua área é de {}m²'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, vocÊ precisará de {}L de tinta'.format(tinta))
