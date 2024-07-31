from fasthtml.common import *
from web3 import Web3, AsyncWeb3
from constants import FOUR_TWENTY_NINE_CONTEST_ABI 

app,rt = fast_app(debug=True)

w3 = Web3(Web3.HTTPProvider('https://mainnet.base.org'))

con = w3.eth.contract(address='0x26cdA3c012779491d33122d0e2cFCe87dd74C254', abi=FOUR_TWENTY_NINE_CONTEST_ABI)

@rt('/props')
def post():
    return str(con.functions.getAllProposalIds().call())

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
    props_button = Button('Get Proposals', id='getprops', cls='col-xs-2', hx_post='/props', target_id="ft2")
    return Div(P('Hello World!', hx_get="/change"), txt, Div(id="ft"), props_button, Div(id="ft2"))

serve()
