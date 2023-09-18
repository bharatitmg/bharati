document.addEventListener("DOMContentLoaded", function () {
    const addPostForm = document.getElementById("addPostForm");

    // Handle form submission to add a new post
    addPostForm.addEventListener("submit", function (event) {
        event.preventDefault();
        const imageSrc = document.getElementById("imageSrc").value;
        const postTitle = document.getElementById("postTitle").value;
        const postContent = document.getElementById("postContent").value;
        const postDescription = document.getElementById("postDescription").value;
        const postKeywords = document.getElementById("postKeywords").value.split(",").map(keyword => keyword.trim());

        const newPost = {
            imageSrc: imageSrc,
            postTitle: postTitle,
            postContent: postContent,
            postDescription: postDescription,
            postKeywords: postKeywords,
        };

        // Send the new post data to the server (PHP script)
        fetch("addpost.php", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(newPost)
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message); // Show a success message from the server
            addPostForm.reset();
        })
        .catch(error => console.error(error));
    });
});
