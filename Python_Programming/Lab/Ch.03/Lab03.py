# page 127
## 과일 가격 계산

price = int(input("정가를 입력하시오> "))
if (price >= 100):
    discountedPrice = price*(0.85)
    print(f'10층에서 선물을 받아가세요.\n상품의 가격: {discountedPrice}')
else:
    discountedPrice = price*(0.9)
    print(f'상품의 가격: {discountedPrice}')