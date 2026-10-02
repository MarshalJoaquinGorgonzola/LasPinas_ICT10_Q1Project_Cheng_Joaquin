from pyscript import document

def createOrder(event):
    subtotal = 0
    prices = {
        "americano": 120,
        "latte": 140,
        "malt": 160,
        "affogato": 150,
        "caramel": 145,
        "papoi": 10000
    }

    if document.querySelector("#americano").checked:
        subtotal += prices["americano"]
    if document.querySelector("#latte").checked:
        subtotal += prices["latte"]
    if document.querySelector("#malt").checked:
        subtotal += prices["malt"]
    if document.querySelector("#affogato").checked:
        subtotal += prices["affogato"]
    if document.querySelector("#caramel").checked:
        subtotal += prices["caramel"]
    if document.querySelector("#papoi").checked:
        subtotal += prices["papoi"]
    vat = subtotal * 0.12
    total = subtotal + vat

    document.querySelector("#receipt").innerHTML = f"""
        <h2>Official Receipt</h2>
        <p>Subtotal: ₱{subtotal:.2f}</p>
        <p>VAT (12%): ₱{vat:.2f}</p>
        <h3>Total Amount: ₱{total:.2f}</h3>
    """