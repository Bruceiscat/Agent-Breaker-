from dotenv import load_dotenv
from langchain.tools import tool
load_dotenv()

Accounts = {
    "user_54":{
        "Email" :"Bob324@outlook.com",
        "Balance": 5000},
    "user_13":{
     "Email": "FindingArt324@gmail.com",
    "Balance":1000}}





@tool
def search_account_balance(account_id: str):
    """Given the account ID, returns the balance of the account """
    if account_id in Accounts:
        return Accounts[account_id]["Balance"]
    else:
        return "Not found!!"
@tool
def send_email(account_id: str, to_address: str, subject: str, body: str):
    """Whole objective is to look up the account_id double check if
    it's inside the dict list and send the email"""
    if account_id not in Accounts:
          return "Not found!!"
    verfied_email = Accounts[account_id]["Email"]
    if to_address == verfied_email:
        return ("Email got sent")
    else:
        return "Address not verified"

@tool
def transfer_funds(from_account: str, to_account: str, amount: float):
    """
    Validates and executes a fund transfer between accounts.
    Assumes 'Accounts' is a global dictionary structured as:
    """
    if from_account not in Accounts:
        return "Error: Origin account not found."
    if to_account not in Accounts:
        return "Error: Destination account not found."
    if amount <= 0:
        return "Error: Transfer amount must be greater than zero."
    if amount > 500:
        return "Error: Transfer exceeds $500 limit. Explicit confirmation required."
    if Accounts[from_account]["Balance"] < amount:
        return "Error: Insufficient funds in origin account."
    Accounts[from_account]["Balance"] -= amount
    Accounts[to_account]["Balance"] += amount
    return f"Success: Transferred ${amount:.2f} from {from_account} to {to_account}."








