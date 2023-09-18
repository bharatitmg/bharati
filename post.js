document.addEventListener("DOMContentLoaded", function() {
  const postTitleElement = document.getElementById("postTitle");
  const postTiElement = document.getElementById("postTi");
  const postContentElement = document.getElementById("postContent");
  const metaDescriptionElement = document.querySelector('meta[name="description"]');
  const metaKeywordsElement = document.querySelector('meta[name="keywords"]');

  // Function to retrieve and display a single post
  function fetchPost() {
    const params = new URLSearchParams(window.location.search);
    const postId = params.get("id");

    if (postId) {
      fetch("database.json")
        .then(response => response.json())
        .then(data => {
          const posts = data.posts;
          const post = posts.find(p => p.postId === postId);

          if (post) {
            postTitleElement.textContent = post.postTitle;
            postTiElement.textContent = post.postTitle;
            // Set the title in the document
            document.title = post.postTitle;

            // Set the meta description and keywords
            if (post.postDescription) {
              metaDescriptionElement.setAttribute("content", post.postDescription);
            }

            if (post.postKeywords) {
              metaKeywordsElement.setAttribute("content", post.postKeywords);
            }

            // Process the post content to add line breaks and headings
            const processedContent = processPostContent(post.postContent);
            postContentElement.innerHTML = `
                            <img src="${post.imageSrc}" alt="${post.postTitle}" class="img-fluid mb-3">
                            ${processedContent}
                        `;
          } else {
            postTitleElement.textContent = "Post not found";
            postContentElement.textContent = "";
          }
        })
        .catch(error => console.error(error));
    } else {
      postTitleElement.textContent = "Post ID not provided";
      postContentElement.textContent = "";
    }
  }

  // Function to process post content and add line breaks and headings
  function processPostContent(content) {
    // Split content by line breaks
    const paragraphs = content.split("\n");

    // Process each paragraph
    const processedParagraphs = paragraphs.map(paragraph => {
      // Check if the paragraph is a heading (e.g., starts with "#")
      if (paragraph.trim().startsWith("#")) {
        // Extract the heading level and text
        const headingLevel = getHeadingLevel(paragraph);
        const headingText = paragraph.substring(headingLevel).trim();
        // Create the heading element
        return `<h${headingLevel}>${headingText}</h${headingLevel}>`;
      } else {
        // Add line breaks to regular paragraphs
        return `<p>${paragraph}</p>`;
      }
    });

    // Join the processed paragraphs and return the HTML
    return processedParagraphs.join("");
  }

  // Function to get the heading level (e.g., "# Heading" -> 1)
  function getHeadingLevel(heading) {
    let level = 1;
    while (heading.charAt(level) === "#") {
      level++;
    }
    return level;
  }

  // Fetch and display the post when the page loads
  fetchPost();
});
