# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
# , and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?

price_per_packet = 1.49  # dollar
total_packets = 9
total_amount = 20
total_price = total_packets * price_per_packet
left_amount = total_amount - total_price
print('The shopkeeper will give me back', left_amount, 'dollar')  # ans.6.59 dollar
