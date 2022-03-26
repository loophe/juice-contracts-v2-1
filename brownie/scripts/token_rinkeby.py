from brownie import accounts, interface, config, JBOperatorStore, JBPrices, JBProjects, JBDirectory, JBFundingCycleStore, JBTokenStore, JBSplitsStore, JBController, JBPaymentTerminalStore, JBETHPaymentTerminal, JBChainlinkV3PriceFeed, JBCurrencies

def main():
    account = accounts.add(config['wallets']['from_key'])
    account1 = accounts.add(config['wallets']['from_key1'])
    cr = interface.JBController('0xC4764344B3026540d14aF0626449f5C5313DC056')
    pr = interface.JBProjects(cr.projects())
    et = interface.JBETHPaymentTerminal('0x14DB44105b43bB9FB9faB6B6b7700ED33693EF10')
    ts = interface.JBTokenStore(cr.tokenStore())
    pt = interface.JBPaymentTerminalStore('0xd6a2C0383dcfE7c516275138FE035269F4a4A534')
    et.pay(0,1,accounts[0],0,False,'loophe','0x00',{'from':accounts[0],'value':10e18})
    cr.issueTokenFor(1,'Monkey King','MKG',{'from':accounts[0]})

