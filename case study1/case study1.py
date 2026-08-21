print(" FOOD DELIVERY ORDER SYSTEM ")
# user  input
#lower we add because nnot to prevent case sensitive 
order_amount = float(input("Enter order amount: "))
distance = float(input("Enter delivery distance: "))
customer_type = input("Enter customer type (Regular/Premium/New): ").lower()
customer_rating = float(input("Enter customer rating: "))
restaurant_rating = float(input("Enter restaurant rating: "))
preparation_time = int(input("Enter preparation time: "))
payment_method = input("Enter payment method (UPI/Card/COD): ").lower()
weather = input("Enter weather (Normal/Rain/Storm): ").lower()
demand = input("Enter demand (Low/Medium/High): ").lower()
peak_hour = input("Is it peak hour? (yes/no): ").lower()
previous_cancellations = int(input("Enter previous cancellations: "))
#########################################################################
##########################################################################
# Delivery charge 
if distance <= 3:
    delivery_charge = 30

    if weather == "rain":
        delivery_charge = delivery_charge + 10
    elif weather == "storm":
        delivery_charge = delivery_charge + 20

elif distance <= 7:
    delivery_charge = 50

    if weather == "rain":
        delivery_charge = delivery_charge + 15
    elif weather == "storm":
        delivery_charge = delivery_charge + 25

else:
    delivery_charge = 80

    if weather == "rain":
        delivery_charge = delivery_charge + 20
    elif weather == "storm":
        delivery_charge = delivery_charge + 30

###############################################################
# Discount
if customer_type == "premium":

    if order_amount >= 500:
        discount = order_amount * 20 / 100
    else:
        discount = order_amount * 10 / 100

elif customer_type == "regular":

    if order_amount >= 500:
        discount = order_amount * 10 / 100
    else:
        discount = 0

elif customer_type == "new":

    if order_amount >= 300:
        discount = order_amount * 15 / 100
    else:
        discount = 50

else:
    discount = 0

#######################################################3
# Restaurant status
if restaurant_rating >= 4.5:

    if preparation_time <= 30:
        restaurant_status = "Excellent"
    else:
        restaurant_status = "Good"

elif restaurant_rating >= 3.5:

    if preparation_time <= 45:
        restaurant_status = "Good"
    else:
        restaurant_status = "Average"

else:
    restaurant_status = "Poor"

#################################################
# Cancellation risk
if previous_cancellations >= 5:
    cancellation_risk = "Very High"

elif previous_cancellations >= 3:
    cancellation_risk = "High"

elif previous_cancellations >= 1:
    cancellation_risk = "Medium"

else:
    cancellation_risk = "Low"

################################################
# Priority delivery
if customer_type == "premium" and customer_rating >= 4:
    priority = "Priority"

elif order_amount >= 700 and preparation_time <= 30:
    priority = "Priority"

elif peak_hour == "yes" and demand == "high":
    priority = "Priority"

else:
    priority = "Normal"

##########################################################33
# Manual review
manual_review = False

if previous_cancellations >= 5:
    manual_review = True

elif customer_rating < 2.5 and order_amount >= 1000:
    manual_review = True

elif weather == "storm" and distance > 10:
    manual_review = True

elif payment_method == "cod" and order_amount >= 2000:
    manual_review = True

#####################################################################
# Order status
if manual_review:
    order_status = "Manual Review"

else:

    if restaurant_rating < 2.5:
        order_status = "Rejected"

    elif preparation_time > 90:
        order_status = "Rejected"

    elif weather == "storm" and distance > 15:
        order_status = "Rejected"

    elif cancellation_risk == "Very High":
        order_status = "Rejected"

    else:

        if customer_rating >= 3 or customer_type == "premium":
            order_status = "Accepted"
        else:
            order_status = "Manual Review"

#############################################################################
# Extra charge
surcharge = 0

if peak_hour == "yes":

    if demand == "high":
        surcharge = 30
    elif demand == "medium":
        surcharge = 15

elif demand == "high":
    surcharge = 20

################################################################################
# Final amount
final_amount = order_amount + delivery_charge + surcharge - discount

if final_amount < 0:
    final_amount = 0

##########################################################################
# Final category
if order_status == "Rejected":
    final_category = "Order Rejected"

elif order_status == "Manual Review":
    final_category = "Requires Manual Verification"

else:

    if priority == "Priority":

        if cancellation_risk == "Low":
            final_category = "Priority Safe Order"
        else:
            final_category = "Priority Risky Order"

    else:

        if cancellation_risk == "High" or cancellation_risk == "Very High":
            final_category = "Normal Risky Order"
        else:
            final_category = "Normal Safe Order"

###########################################################3
# Final report which is generate 
print("FINAL ORDER REPORT ")

print("Order Amount         :", order_amount)
print("Delivery Distance    :", distance, "km")
print("Delivery Charge      :", delivery_charge)
print("Demand Surcharge     :", surcharge)
print("Discount             :", discount)

print("----------------------------------------")

print("Order Status         :", order_status)
print("Priority Delivery    :", priority)
print("Cancellation Risk    :", cancellation_risk)
print("Restaurant Status    :", restaurant_status)

if manual_review:
    print("Manual Review Status : Required")
else:
    print("Manual Review Status : Not Required")

print("Final Order Category :", final_category)
print("Final Payable Amount :", round(final_amount, 2))

print("===================================================")