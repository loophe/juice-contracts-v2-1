from brownie import accounts, interface, config, JBOperatorStore, JBPrices, JBProjects, JBDirectory, JBFundingCycleStore, JBTokenStore, JBSplitsStore, JBController, JBPaymentTerminalStore, JBETHPaymentTerminal, JBChainlinkV3PriceFeed, JBCurrencies, JBERC20PaymentTerminal

def main():
    # account = accounts.add(config['wallets']['from_key'])
    # account1 = accounts.add(config['wallets']['from_key1'])
   
    USD = interface.daiInterface('0x6b175474e89094c44da98b954eedeac495271d0f') #DAI mainnet
    FUND = 1000000e18
    USD.mint(accounts[0],FUND,{'from':'0x9759A6Ac90977b93B58547b4A71c78317f391A28'})
    balU = USD.balanceOf(accounts[0])
    print(f'User has USD balance is {balU/1e18}\n')
    os = JBOperatorStore.deploy({'from':accounts[0]})
    pc = JBPrices.deploy(accounts[0],{'from':accounts[0]})
    pr = JBProjects.deploy(os,{'from':accounts[0]})
    dr = JBDirectory.deploy(os,pr,accounts[0],{'from':accounts[0]})
    fc = JBFundingCycleStore.deploy(dr,{'from':accounts[0]})
    ts = JBTokenStore.deploy(os,pr,dr,{'from':accounts[0]})
    ps = JBSplitsStore.deploy(os,pr,dr,{'from':accounts[0]})
    cr = JBController.deploy(os,pr,dr,fc,ts,ps,{'from':accounts[0]})
    dr.setIsAllowedToSetFirstController(cr,True,{'from':accounts[0]})
    pt = JBPaymentTerminalStore.deploy(pc,dr,fc,{'from':accounts[0]})
    # et = JBETHPaymentTerminal.deploy(1,os,pr,dr,ps,pc,pt,accounts[0],{'from':accounts[0]})
   
    print(f'ERC20PaymentTermianl deploying...')
    ec = JBERC20PaymentTerminal.deploy(USD,2,1,3,os,pr,dr,ps,pc,pt,accounts[0],{'from':accounts[0]})
    print(f'ERC20PaymentTerminal has deployed at {ec}\n')
    lc = JBCurrencies.deploy({'from':accounts[0]})    
    ch = JBChainlinkV3PriceFeed.deploy('0x773616E4d11A78F511299002da57A0a94577F1f4',{'from':accounts[0]}) #Mainnet fork
    pc.addFeedFor(lc.USD(),lc.ETH(),ch,{'from':accounts[0]})
    # cr.launchProjectFor(accounts[0],['',0],[1209600,1e25,40000000,'0x0000000000000000000000000000000000000000'],[5000,7000,7000,False,False,False,False,False,False,False,False,False,False,False,False,'0x0000000000000000000000000000000000000000'],0,[],[],[et],'',{'from':accounts[0]})
    cr.launchProjectFor(accounts[0],['',0],[1209600,100e18,40000000,'0x0000000000000000000000000000000000000000'],[5000,7000,7000,False,False,False,False,False,False,False,False,False,False,False,False,'0x0000000000000000000000000000000000000000'],0,[],[],[ec],'',{'from':accounts[0]})
    balp = pr.balanceOf(accounts[0])
    print(f'Controller launch project {balp}.\n')
    # et.pay(0,1,accounts[0],0,False,'loophe','0x00',{'from':accounts[0],'value':10e18})
    USD.approve(ec,FUND,{'from':accounts[0]})
    print(f'User pay Fund to ERC20PaymentTerminal.')
    ec.pay(FUND,1,accounts[0],0,False,'','0x00',{'from':accounts[0]})
    
    cr.issueTokenFor(1,'Monkey King','MKG',{'from':accounts[0]})
    bal = ts.balanceOf(accounts[0],1)
    tokenAddress = ts.tokenOf(1)
    to = interface.JBToken(tokenAddress)
    symbol = to.symbol()
    ts.claimFor(accounts[0],1,bal,{'from':accounts[0]})
    balt = to.balanceOf(accounts[0])
    print(f'\nUser has {symbol} token balance is {balt/1e18}.\n')


    




    
