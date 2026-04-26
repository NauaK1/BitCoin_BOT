import ssl
import json

import websocket

def ao_abrir(ws):
    print("Abriu Conexão")

    json_subs = """
{
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd"
    }
}

"""
    ws.send(json_subs)

def ao_fechar(ws):
    print("Fechou Conexão")


def erro(ws, erro):
    print("Deu erro na Conexão")
    print(erro)


def ao_receber_mensagem(ws, msg):
    msg = json.loads(msg)
    print(msg["data"]["price"]) #preço



if __name__=="__main__":
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net",
                                on_open=ao_abrir,
                                on_error=erro,
                                on_message=ao_receber_mensagem,
                                on_close=ao_fechar)
    
    ws.run_forever(sslopt={"cert_regs":ssl.CERT_NONE})