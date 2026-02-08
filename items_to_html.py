from item import load_items

HTML_FILE = 'items.html'

def generate_html(items):
    rows = ""
    for item in items:
        rows += f"""
        <tr>
            <td>{item.department}</td>
            <td>{item.division}</td>
            <td>{item.itemcode}</td>
            <td>{item.name}</td>
            <td>{item.season}</td>
            <td>{item.material}</td>
            <td>{item.price}</td>
            <td>{item.limited_offer}</td>
            <td>{item.sale}</td>
            <td>{item.stock}</td>
        </tr>
        """

    return f"""
    <!DOCTYPE html>
    <head>
    <link rel="stylesheet" href="main.css">
    </head>
    <body>
        <h1>Acme</h1>
        <header>
        <p>Current item catalog</p>
        </header>
        <table border="1">
            <tr>
                <th>Department</th>
                <th>Division</th>
                <th>Itemcode</th>
                <th>Name</th>
                <th>Season</th>
                <th>Material</th>
                <th>Price</th>
                <th>Limited offer</th>
                <th>Sale</th>
                <th>Current stock</th>
            </tr>
            {rows}
        </table>
    </body>
    </html>
    """

def main():
    items = load_items()
    html = generate_html(items)

    with open(HTML_FILE, "w") as f:
        f.write(html)

if __name__ == "__main__":
    main()