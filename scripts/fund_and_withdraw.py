from brownie import FundMe
from scripts.tools import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS

def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding the contract ...")
    fund_me.fund({"from": account, "value": entrance_fee})
    
def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})
    
def main():
    fund()
    withdraw()