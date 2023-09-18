document.addEventListener("DOMContentLoaded", function() {
  const blogPostsContainer = document.getElementById("blogPosts");
  const paginationContainer = document.getElementById("pagination");
  const postsPerPage = 12; // Number of posts per page

  // Function to fetch and display existing posts
  function fetchExistingPosts() {
    fetch("database.json")
      .then(response => response.json())
      .then(data => {
        const posts = data.posts;

        // Calculate the total number of pages
        const totalPages = Math.ceil(posts.length / postsPerPage);

        // Get the current page from the query string or default to page 1
        const params = new URLSearchParams(window.location.search);
        const currentPage = parseInt(params.get("page")) || 1;

        // Calculate the starting and ending indices for pagination
        const startIndex = (currentPage - 1) * postsPerPage;
        const endIndex = startIndex + postsPerPage;

        // Display posts for the current page
        const currentPosts = posts.slice(startIndex, endIndex);

        if (currentPosts.length === 0) {
          blogPostsContainer.innerHTML = "<p>No posts found.</p>";
        } else {
          currentPosts.forEach(post => {
            const postDiv = document.createElement("div");
            postDiv.classList.add("col-md-4", "mb-4");
            postDiv.innerHTML = `
                            <div class="card">
                                <img src="${post.imageSrc}" class="card-img-top" alt="${post.postTitle}">
                                <div class="card-body">
                                    <h5 class="card-title"><a href="post.html?id=${post.postId}">${post.postTitle}</a></h5>
                                    <p class="card-text">${post.postDescription}</p>
                                </div>
                            </div>
                        `;
            blogPostsContainer.appendChild(postDiv);
          });
        }

        // Generate pagination links
        const paginationHTML = [];
        for (let i = 1; i <= totalPages; i++) {
          const activeClass = i === currentPage ? "active" : "";
          paginationHTML.push(`<li class="page-item ${activeClass}"><a class="page-link" href="?page=${i}">${i}</a></li>`);
        }
        paginationContainer.innerHTML = paginationHTML.join("");
      })
      .catch(error => console.error(error));
  }

  // Fetch and display existing posts when the page loads
  fetchExistingPosts();
});
