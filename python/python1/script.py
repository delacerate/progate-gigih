apple_price = 2
# Berikan 10 ke variable money 


input_count = input('Mau berapa apel?: ')
count = int(input_count)
total_price = apple_price * count

print('Anda akan membeli ' + str(count) + ' apel')
print('Harga total adalah ' + str(total_price) + ' dolar')

# Tambahkan control flow berdasarkan perbandingan antara money dan total_price
money = 10
if money > total_price:
  print('Anda telah membeli ' + str(count) + 'apel')
  print('Uang Anda tinggal ' + str(total_price) + 'dolar')
elif money == total_price:
  print('Anda telah membeli ' + str(count) + 'apel')
  print('Dompet Anda kosong')
else:
  print('Uang Anda tidak mencukupi')
  print('Anda tidak dapat membeli apel sebanyak itu')
