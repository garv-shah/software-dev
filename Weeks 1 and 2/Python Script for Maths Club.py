from bs4 import BeautifulSoup
import re

html_in = """
<p>We know that the perimeters of the two small triangles are <img src="//latex.artofproblemsolving.com/b/5/c/b5c9baf49e329e4da7080a38964943e1968e7824.png" class="latex" alt="$3+CD+AD$" style="vertical-align: -1px" width="112" height="14"> and <img src="//latex.artofproblemsolving.com/6/c/6/6c66b39f52c2df8bba0e7f3c9765624b37f4b59d.png" class="latex" alt="$4+BD+AD$" style="vertical-align: -1px" width="112" height="14">. Setting both equal and using <img src="//latex.artofproblemsolving.com/7/2/1/7211af31ccf32bcb08df8e89df65a86ce9b129df.png" class="latex" alt="$BD+CD = 5$" style="vertical-align: -1px" width="115" height="14">, we have <img src="//latex.artofproblemsolving.com/d/0/a/d0ae22fbe6167df969d0b1f9a698029e6774c45a.png" class="latex" alt="$BD = 2$" width="63" height="12"> and <img src="//latex.artofproblemsolving.com/b/5/3/b53e0064e5c0075ceeb38a4e29b4fa1ed396dd85.png" class="latex" alt="$CD = 3$" width="62" height="12">. Now, we simply have to find the area of <img src="//latex.artofproblemsolving.com/f/7/5/f75d6d58b03031bd7cb52a7ca886a8ddf369d21c.png" class="latex" alt="$\triangle ABD$" width="59" height="13">. Since <img src="//latex.artofproblemsolving.com/d/8/8/d8856a7429d98abb14ef48fc8550c0375408cec7.png" class="latex" alt="$\frac{BD}{CD} = \frac{2}{3}$" style="vertical-align: -12px" width="70" height="37">, we must have <img src="//latex.artofproblemsolving.com/a/d/b/adbd8883f0cd8632fcfbbf06047ae4d60076fef4.png" class="latex" alt="$\frac{[ABD]}{[ACD]} = 2/3$" style="vertical-align: -17px" width="108" height="43">. Combining this with the fact that <img src="//latex.artofproblemsolving.com/7/d/8/7d8610994146054d34d9933863709ec1574f11f1.png" class="latex" alt="$[ABC] = [ABD] + [ACD] = \frac{3\cdot4}{2} = 6$" style="vertical-align: -12px" width="299" height="37">, we get <img src="//latex.artofproblemsolving.com/a/a/5/aa5e715c3874487c0abd4ed1151a562b3058d244.png" class="latex" alt="$[ABD] = \frac{2}{5}[ABC] = \frac{2}{5} \cdot 6 = \boxed{\textbf{(D) } \frac{12}{5}}$" style="vertical-align: -18px" width="297" height="48">
</p>
"""
soup = BeautifulSoup(html_in, "html.parser")
imgs = soup.findAll('img')
alt_list = []

for x in imgs:
    alt_list.append(x.get('alt'))

img_split = re.split("<img[^>]*>", html_in)

final_array = [None]*(len(img_split)+len(alt_list))
final_array[::2] = img_split
final_array[1::2] = alt_list

print("".join(final_array).replace("'", ""))
