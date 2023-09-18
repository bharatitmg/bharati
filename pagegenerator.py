import json
from jinja2 import Template
import re
# Read data from database.json
with open('database.json', 'r') as file:
    data = json.load(file)

# Load the HTML template
template = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <link rel="apple-touch-icon" sizes="76x76" href="./assets/img/favicon.ico">
    <link rel="icon" type="image/png" href="./assets/img/favicon.ico">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <title>{{ postTitle }} - Bijayakumartamang.com.np </title>
    <meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0, shrink-to-fit=no" name="viewport">
    <meta name="description" content="{{ postDescription }}">
    <meta name="keywords" content="{{ postKeywords }}">
    <!-- Google Font -->
    <link href="https://fonts.googleapis.com/css?family=Playfair+Display:400,700|Source+Sans+Pro:400,700" rel="stylesheet">
    <!-- Font Awesome Icons -->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css" integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU" crossorigin="anonymous">
    <!-- Main CSS -->
    <link href="./assets/css/main.css" rel="stylesheet">
                    <script async src="https://www.googletagmanager.com/gtag/js?id=G-PDQY576ZSW"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag() {dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-PDQY576ZSW');
  </script>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9631856282418168"
    crossorigin="anonymous"></script>
</head>
<body>
<nav class="topnav navbar navbar-expand-lg navbar-light bg-white fixed-top">
    <div class="container">
        <a class="navbar-brand" href="./index.html"><strong>Bijayakumartamang.com.np</strong></a>
        <button class="navbar-toggler collapsed" type="button" data-toggle="collapse" data-target="#navbarColor02" aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="navbar-collapse collapse" id="navbarColor02" style="">
            <ul class="navbar-nav mr-auto d-flex align-items-center">
                <li class="nav-item">
                    <a class="nav-link" href="index.html">Home</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="about.html">About</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="newshome.html">News</a>
                </li>
            </ul>
        </div>
    </div>
</nav>

<div class="container mt-5">
    <!-- Post content -->
    <div class="post-content">
        <h1>{{ postTitle }}</h1>
                    <div class="ad-placeholder"><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9631856282418168" crossorigin="anonymous"></script>
                 <!-- bj -->
                 <ins class="adsbygoogle"
                      style="display:block"
                      data-ad-client="ca-pub-9631856282418168"
                      data-ad-slot="9450638780"
                      data-ad-format="auto"
                      data-full-width-responsive="true"></ins>
                 <script>
                      (adsbygoogle = window.adsbygoogle || []).push({});
                 </script></div>
        <img src="{{ imageSrc }}" alt="{{ postTitle }}" class="img-fluid">
        
                    <div class="ad-placeholder"><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9631856282418168" crossorigin="anonymous"></script>
                 <!-- bj -->
                 <ins class="adsbygoogle"
                      style="display:block"
                      data-ad-client="ca-pub-9631856282418168"
                      data-ad-slot="9450638780"
                      data-ad-format="auto"
                      data-full-width-responsive="true"></ins>
                 <script>
                      (adsbygoogle = window.adsbygoogle || []).push({});
                 </script></div>
        {{ postContent }}
    </div>
    <div class="col-lg-6">
			<div class="ad-placeholder"><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9631856282418168" crossorigin="anonymous"></script>
                 <!-- bj -->
                 <ins class="adsbygoogle"
                      style="display:block"
                      data-ad-client="ca-pub-9631856282418168"
                      data-ad-slot="9450638780"
                      data-ad-format="auto"
                      data-full-width-responsive="true"></ins>
                 <script>
                      (adsbygoogle = window.adsbygoogle || []).push({});
                 </script></div>
				<div class="ad-placeholder"><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9631856282418168" crossorigin="anonymous"></script>
                 <!-- bj -->
                 <ins class="adsbygoogle"
                      style="display:block"
                      data-ad-client="ca-pub-9631856282418168"
                      data-ad-slot="9450638780"
                      data-ad-format="auto"
                      data-full-width-responsive="true"></ins>
                 <script>
                      (adsbygoogle = window.adsbygoogle || []).push({});
                 </script></div>
				<div class="ad-placeholder"><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9631856282418168" crossorigin="anonymous"></script>
                 <!-- bj -->
                 <ins class="adsbygoogle"
                      style="display:block"
                      data-ad-client="ca-pub-9631856282418168"
                      data-ad-slot="9450638780"
                      data-ad-format="auto"
                      data-full-width-responsive="true"></ins>
                 <script>
                      (adsbygoogle = window.adsbygoogle || []).push({});
                 </script></div>
			</div>
		</div>
</div>
<!-- End Content -->
<div class="container">
	<div class="row justify-content-between">
		<div class="col-md-8">
			<h5 class="font-weight-bold spanborder"><span>All Stories</span></h5>
			<div class="mb-3 d-flex justify-content-between">
				<div class="pr-3">
					<h2 class="mb-1 h4 font-weight-bold">
					<a class="text-dark" href="detail_6507d537f0e9e.html">How to overcome anxiety</a>
					</h2>
					<p>
						Anxiety is a pervasive and often debilitating condition...
					</p>
					<div class="card-text text-muted small">
						 Bijayakumartamang.com.np
					</div>
					<small class="text-muted">Dec 12 &middot; 5 min read</small>
				</div>
				<img height="120" src="https://cdn.pixabay.com/photo/2017/08/21/19/00/woman-2666433_1280.jpg">
			</div>
			<div class="mb-3 d-flex justify-content-between">
				<div class="pr-3">
					<h2 class="mb-1 h4 font-weight-bold">
					<a class="text-dark" href="detail_2023-09-03_17_53_46.html">Excitement Builds as India and Nepal Clash in Asia Cup 2023</a>
					</h2>
					<p>
						India enters the contest as the undisputed favorites.
					</p>
					<div class="card-text text-muted small">
						 Bijayakumartamang.com.np
					</div>
					<small class="text-muted">Dec 12 &middot; 5 min read</small>
				</div>
				<img height="120" src="https://images.indianexpress.com/2023/09/India-vs-Nepal.jpg">
			</div>
			<div class="mb-3 d-flex justify-content-between">
				<div class="pr-3">
					<h2 class="mb-1 h4 font-weight-bold">
					<a class="text-dark" href="detail_2023-08-04_06_19_46.html">In an increasingly urbanized and digitally connected world</a>
					</h2>
					<p>
						In an increasingly urbanized and digitally connected world....
					</p>
					<div class="card-text text-muted small">
						 Bijayakumartamang.com.np
					</div>
					<small class="text-muted">Dec 12 &middot; 5 min read</small>
				</div>
				<img height="120" src="https://cdn.pixabay.com/photo/2016/05/10/21/50/meditation-1384758_1280.jpg">
			</div>
		</div>
		<div class="col-md-4 pl-4">
            <h5 class="font-weight-bold spanborder"><span>Popular</span></h5>
			<ol class="list-featured">
				<li>
				<span>
				<h6 class="font-weight-bold">
				<a href="detail_2023-08-04_05_45_29.html" class="text-dark">The Future of Work: Navigating Automation and the Rise of AI</a>
				</h6>
				<p class="text-muted">
					Bijayakumartamang.com.np
				</p>
				</span>
				</li>
				<li>
				<span>
				<h6 class="font-weight-bold">
				<a href="detail_2023-08-04_04_33_31.html" class="text-dark">Mindfulness: A Path to Inner Peace and Emotional Well-Being</a>
				</h6>
				<p class="text-muted">
					Bijayakumartamang.com.np
				</p>
				</span>
				</li>
				<li>
				<span>
				<h6 class="font-weight-bold">
				<a href="detail_64f98d2f471c9.html" class="text-dark">Ryan Gravenberch's Early Commitment to Liverpool: A Sign of Things to Come</a>
				</h6>
				<p class="text-muted">
					Bijayakumartamang.com.np
				</p>
				</span>
				</li>
				<li>
				<span>
				<h6 class="font-weight-bold">
				<a href="detail_64f9ad6b9ea60.html" class="text-dark">AlphaGo Zero: Redefining AI Mastery in the World of Go</a>
				</h6>
				<p class="text-muted">
					Bijayakumartamang.com.np
				</p>
				</span>
				</li>
			</ol>
		</div>
	</div>
</div>
<div class="container mt-5">
	<footer class="bg-white border-top p-3 text-muted small">
	<div class="row align-items-center justify-content-between">
		<div>
			<span class="navbar-brand mr-2"><strong>Bijayakumartamang.com.np</strong></span> Copyright &copy;
			<script>document.write(new Date().getFullYear())</script>
			 . All rights reserved.
		</div>
		<div>
			 Made with <a target="_blank" class="text-secondary font-weight-bold" href="index.html">Bijayakumartamang.com.np</a> 
		</div>
	</div>
	</footer>
</div>
<!-- End Footer -->
<!-- JAVASCRIPTS -->
<script src="./assets/js/vendor/jquery.min.js" type="text/javascript"></script>
<script src="./assets/js/vendor/popper.min.js" type="text/javascript"></script>
<script src="./assets/js/vendor/bootstrap.min.js" type="text/javascript"></script>
<script src="./assets/js/functions.js" type="text/javascript"></script>
</body>
</html>

""")

# Process each post and generate a separate HTML file
for post in data['posts']:
    post_title = post['postTitle']
    post_description = post['postDescription']
    post_keywords = post['postKeywords']
    image_src = post['imageSrc']
    post_content = post['postContent']
    post_content = re.sub(r'\n', '<br>', post_content)
    # Create a dictionary with template variables
    template_vars = {
        'postTitle': post_title,
        'postDescription': post_description,
        'postKeywords': post_keywords,
        'imageSrc': image_src,
        'postContent': post_content
    }

    # Render the template with the post data
    rendered_html = template.render(**template_vars)

    # Generate a unique HTML filename for each post
    html_filename = f'detail_{post["postId"]}.html'
    html_filename = re.sub(r'[\/:*?"<>| ]', '_', html_filename)
    # Save the rendered HTML to a file
    with open(html_filename, 'w', encoding='utf-8') as html_file:
        html_file.write(rendered_html)

    print(f'Generated {html_filename}')

print("HTML files generated successfully.")
