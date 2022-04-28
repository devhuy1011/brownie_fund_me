from brownie import accounts
from scripts.tools import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def test_can_fund_and_withdraw():
    account = get_account()