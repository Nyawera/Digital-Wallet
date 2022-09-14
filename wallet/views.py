from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import CustomerCurrencyForm, CustomerLoanForm, CustomerNotificationsForm, CustomerReceiptForm, CustomerRegistrationForm, CustomerRewardForm, CustomerThird_partyForm
from .forms import CustomerWalletForm
from .forms import CustomerAccountForm
from .forms import CustomerTransactionForm
from .forms import CustomerCardForm
from  .models import Customer

def register_customer(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
         if form.is_valid():
            form.save()
else:
  
    form = CustomerRegistrationForm()
    return render (request,"wallet/register_customer.html",
    {"form":form})

def customer_wallet(request):
    form = CustomerWalletForm()
    return render(request,"wallet/customer_wallet.html",
    {"form":form})

def customer_account(request):
    form = CustomerAccountForm()
    return render(request,"wallet/customer_account.html",
    {"form":form})

def customer_transaction(request):
    form = CustomerTransactionForm()
    return render(request,"wallet/customer_transaction.html",
    {"form":form})

def customer_card(request):
    form = CustomerCardForm()
    return render(request,"wallet/customer_card.html",
    {"form":form})    
    
def customer_thirdparty(request):
    form = CustomerThird_partyForm()
    return render(request,"wallet/customer_thirdparty.html",
    {"form":form})    

def customer_notifications(request):
    form = CustomerNotificationsForm()
    return render(request,"wallet/customer_notifications.html",
    {"form":form})  

def customer_receipts(request):
    form = CustomerReceiptForm()
    return render(request,"wallet/customer_receipt.html",
    {"form":form})    

def customer_loan(request):
    form = CustomerLoanForm()
    return render(request,"wallet/customer_loan.html",
    {"form":form})     

def customer_reward(request):
    form = CustomerRewardForm()
    return render(request,"wallet/customer_reward.html",
    {"form":form})     

def customer_currency(request):
    form = CustomerCurrencyForm()
    return render(request,"wallet/customer_currency.html",
    {"form":form})         

def list_customers(request):
    customers=Customer.objects.all()
    return render(request, "wallet/customerlist.html")
    {"customers":customers}