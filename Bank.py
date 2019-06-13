class Account:
	
	def __init__(self,owner,balance=0):
		self.owner = owner
		self.balance = balance
		
	def deposit(self,dep_amt):
		self.balance=self.balance+dep_amt
		print("Added {} to the balance".format(dep_amt))
		
	def withdraw(self,wd_amt):
		if(wd_amt<=self.balance):
			self.balance=self.balance-wd_amt
			print('Withdrawal accepted')
		else:
			print("Sorry not enough funds")
	
	def __str__(self):
		return "Owner: {} \nBalances: {}".format(self.owner,self.balance)




#Tests
# 1. Instantiate the class
acct1 = Account('Jose',100)
# 2. Print the object
print(acct1)
# 3. Show the account owner attribute
acct1.owner
# 4. Show the account balance attribute
acct1.balance
# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
acct1.withdraw(75)
# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)