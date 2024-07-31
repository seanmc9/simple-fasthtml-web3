from fasthtml.common import *
from web3 import Web3, AsyncWeb3

app,rt = fast_app()

w3 = Web3(Web3.HTTPProvider('https://mainnet.base.org'))
abi = '[{"type":"function","name":"version","inputs":[],"outputs":[{"name":"","type":"string","internalType":"string"}],"stateMutability":"pure"}]'

con = w3.eth.contract(address='0x26cdA3c012779491d33122d0e2cFCe87dd74C254', abi=abi)

@rt('/submit')
def post(html: str): 
    return html

@rt('/change')
def get(): 
    block_num = w3.eth.get_block('latest').number
    version = con.functions.version().call()
    return P('Nice to be here!', block_num, version)

@rt('/')
def get():
    txt = Textarea(id="html", rows=10, hx_post='/submit', target_id="ft", hx_trigger='keyup delay:500ms')
    return Div(P('Hello World!', hx_get="/change"), txt, Div(id="ft"))

serve()
