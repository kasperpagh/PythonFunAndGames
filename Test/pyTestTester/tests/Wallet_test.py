from entities.Wallet import Wallet
import pytest


@pytest.fixture
def wallet():
    testWallet = Wallet(500, 1234)
    return testWallet


@pytest.fixture
def emptyWallet():
    testWallet = Wallet(0, 1234)
    return testWallet


@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_parameterCase(emptyWallet, earned, spent, expected):
    emptyWallet.addMoney(earned)
    emptyWallet.withdraw(spent, 1234)
    assert emptyWallet.checkBalance(1234) == expected


def test_walletIntegrety_00(wallet):
    assert wallet.balance == 500
    assert wallet.pincode == 1234


def test_walletIntegrety_01(wallet):
    with pytest.raises(Exception):
        wallet.checkBalance(1234523432)


def test_walletIntegrety_02(wallet):
    with pytest.raises(Exception):
        wallet.checkBalance()


def test_walletIntegrety_03(wallet):
    with pytest.raises(Exception):
        wallet.checkBalance("john")


def test_checkBalance_00(wallet):
    assert wallet.balance == 500


def test_checkBalance_01(wallet):
    wallet = Wallet(250, 213123)
    assert wallet.balance == 250


def test_addAndWithdraw__00(wallet):
    wallet.withdraw(250, 1234)
    assert wallet.balance == 250


def test_addAndWithdraw__01(wallet):
    wallet.withdraw(500, 1234)
    assert wallet.balance == 0


def test_addAndWithdraw__02(wallet):
    wallet.withdraw(500, 1234)
    assert wallet.balance == 0


def test_addAndWithdraw__03(wallet):
    with pytest.raises(Exception):
        wallet.withdraw(501, 1234)
