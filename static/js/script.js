// mobile navmenu button
const navmenu = document.querySelector(".menu-btn");
const bar1 = document.querySelector(".bar1");
const bar2 = document.querySelector(".bar2");
const bar3 = document.querySelector(".bar3");
const menu = document.querySelector(".menu");
navmenu.addEventListener("click", () => {
  bar1.classList.toggle("baranimation1");
  bar2.classList.toggle("baranimation2");
  bar3.classList.toggle("baranimation3");
  menu.classList.toggle("active");
});

// alert card
document.addEventListener("DOMContentLoaded", function () {
  var alertElements = document.querySelectorAll(".alert");

  alertElements.forEach(function (alertElement) {
    alertElement.classList.add("active");

    setTimeout(function () {
      alertElement.classList.remove("active");
    }, 6000); // 6 saniye sonra 'active' sınıfını kaldırır (süreyi isteğinize göre ayarlayabilirsiniz)
  });
});

// blog page search bar
function Search(searchText) {
  var searchResults = document.getElementById('searchResults');
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
          var results = JSON.parse(xhr.responseText);

          var resultsHTML = '';
          if (results.length > 0) {
              for (var i = 0; i < results.length; i++) {
                  resultsHTML += '<li><a class="resulItem" href="">' + results[i] + '</a></li>';
              }
          } else {
              resultsHTML = '<p>No result found</p>';
          }

          searchResults.innerHTML = resultsHTML;
      }
  };
  xhr.open('GET', '/search/?query=' + encodeURIComponent(searchText));
  xhr.send();
}

// modal scripting
