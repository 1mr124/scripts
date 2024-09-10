import requests
from lxml import html

url = "https://natega.cpyp.net/Home/Natega"
headers = {
    "Host": "natega.cpyp.net",
    "Cookie": "_ga_GJH4KCV03B=GS1.1.1722912237.1.0.1722912237.0.0.0; _ga=GA1.1.813766488.1722912237; __gads=ID=13372f111713a6e5:T=1722912238:RT=1722912238:S=ALNI_MboiXWWYjjJepDy9FuhCEtGMDsATw; __gpi=UID=00000ebba1d74627:T=1722912238:RT=1722912238:S=ALNI_MZenpCTn9CGPWD_x7Vk1_D9cCZnuQ; __eoi=ID=19c0c6284672f3a7:T=1722912238:RT=1722912238:S=AA-AfjYdM6qsxXuE1yA8O-MZ728O; _ga_5LP8VJKL83=GS1.1.1722912237.1.1.1722912278.0.0.0",
    "Accept-Language": "en-US",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "https://natega.cpyp.net",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36",
    "Referer": "https://natega.cpyp.net/",

}

# Range of seating numbers
start_seating_no = 634646
end_seating_no = 634667

for seating_no in range(631000, 635000):
    payload = f"seating_no={seating_no}"
    
    response = requests.post(url, headers=headers, data=payload)
    
    # Parse the response content
    tree = html.fromstring(response.content)
    
    # Extract the element using XPath
    element = tree.xpath('/html/body/div[1]/div[6]/div[1]/div[1]/div[5]/ul/li[1]/span[2]')
    with open("3amFatch3alek.txt","a")as f: 
        if element:
            element_content = html.tostring(element[0], pretty_print=True, encoding='unicode')
            
            # Print the element content
            print(f"Content for seating number {seating_no}:{element_content.replace("<span>","").replace("</span>","")}")
            f.write(f"{seating_no}:\n{element_content.replace("<span>","").replace("</span>","")}\n")
        else:
            print(f"Element not found for seating number {seating_no}")
