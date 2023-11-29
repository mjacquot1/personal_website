/**
* Template Name: iPortfolio
* Updated: Sep 18 2023 with Bootstrap v5.3.2
* Template URL: https://bootstrapmade.com/iportfolio-bootstrap-portfolio-websites-template/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
(function () {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select('#navbar .scrollto', true)
  const navbarlinksActive = () => {
    let position = window.scrollY + 200
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return
      let section = select(navbarlink.hash)
      if (!section) return
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active')
      } else {
        navbarlink.classList.remove('active')
      }
    })
  }
  window.addEventListener('load', navbarlinksActive)
  onscroll(document, navbarlinksActive)

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    let elementPos = select(el).offsetTop
    window.scrollTo({
      top: elementPos,
      behavior: 'smooth'
    })
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Mobile nav toggle
   */
  on('click', '.mobile-nav-toggle', function (e) {
    select('body').classList.toggle('mobile-nav-active')
    this.classList.toggle('bi-list')
    this.classList.toggle('bi-x')
  })

  /**
   * Scrool with ofset on links with a class name .scrollto
   */
  on('click', '.scrollto', function (e) {
    if (select(this.hash)) {
      e.preventDefault()

      let body = select('body')
      if (body.classList.contains('mobile-nav-active')) {
        body.classList.remove('mobile-nav-active')
        let navbarToggle = select('.mobile-nav-toggle')
        navbarToggle.classList.toggle('bi-list')
        navbarToggle.classList.toggle('bi-x')
      }
      scrollto(this.hash)
    }
  }, true)

  /**
   * Scroll with ofset on page load with hash links in the url
   */
  window.addEventListener('load', () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash)
      }
    }
  });

  /**
   * Hero type effect
   */
  const typed = select('.typed')
  if (typed) {
    let typed_strings = typed.getAttribute('data-typed-items')
    typed_strings = typed_strings.split(',')
    new Typed('.typed', {
      strings: typed_strings,
      loop: true,
      typeSpeed: 100,
      backSpeed: 50,
      backDelay: 2000
    });
  }

  /**
   * Porfolio isotope and filter
   */
  window.addEventListener('load', () => {
    let recreationContainer = select('.recreation-container');
    if (recreationContainer) {
      let recreationIsotope = new Isotope(recreationContainer, {
        itemSelector: '.recreation-item'
      });

      let recreationFilters = select('#recreation-filter li', true);

      on('click', '#recreation-filter li', function (e) {
        e.preventDefault();
        recreationFilters.forEach(function (el) {
          el.classList.remove('filter-active');
        });
        this.classList.add('filter-active');

        recreationIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        recreationIsotope.on('arrangeComplete', function () {
          AOS.refresh()
        });
      }, true);
    }

  });

  /**
   * Initiate portfolio lightbox 
   */
  const portfolioLightbox = GLightbox({
    selector: '.portfolio-lightbox'
  });

  /**
   * Portfolio details slider
   */
  new Swiper('.portfolio-details-slider', {
    speed: 400,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
  });

  /**
   * Testimonials slider
   */
  new Swiper('.testimonials-slider', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 20
      },

      1200: {
        slidesPerView: 3,
        spaceBetween: 20
      }
    }
  });

  /**
   * Animation on scroll
   */
  window.addEventListener('load', () => {
    AOS.init({
      duration: 1000,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    })
  });

  /**
   * Initiate Pure Counter 
   */
  new PureCounter();

}

)()
/* 
-----TO DO-----

- Change _ case to camelcase
- Add error handlers for
-- No 'resume_accordion' classes
-- No 'resume_line_detail' classes
-- No 'data-filters' classes


*/


const resumeBlockList = document.getElementsByClassName("resume_accordion");
const resumeLineList = document.getElementsByClassName("resume_line_detail");

const activeResumeFilters = [];

const resumeCategoryElements = {
  resumeBlocks : {},
  resumeLines : {},
};

function isEmpty(value) {
  return (value == null || (typeof value === "string" && value.trim().length === 0));
}

function isNotEmpty(value) {
  return (value != null || (typeof value === "string" && value.trim().length != 0));
}

function returnAttributeValue(element, attribute) {
  // Return empty string if no attribute
  return isNotEmpty(element.getAttribute(attribute)) ? element.getAttribute(attribute) : ''
}

window.onload = function() {
  for (let i = 0; i < resumeBlockList.length; i++){
    if (isNotEmpty(resumeBlockList[i])) {
      returnAttributeValue(resumeBlockList[i], 'data-filters').split(' ').forEach((category) => {
        if (resumeCategoryElements.resumeBlocks.hasOwnProperty(category)) {
          resumeCategoryElements.resumeBlocks[category].push(resumeBlockList[i]);
        } else {
          resumeCategoryElements.resumeBlocks[category] = [resumeBlockList[i]];
        }
      })
    }
  }

  for (let i = 0; i < resumeLineList.length; i++){
    if (isNotEmpty(resumeLineList[i])) {
      returnAttributeValue(resumeLineList[i], 'data-filters').split(' ').forEach((category) => {
        if (resumeCategoryElements.resumeLines.hasOwnProperty(category)) {
          resumeCategoryElements.resumeLines[category].push(resumeLineList[i]);
        } else {
          resumeCategoryElements.resumeLines[category] = [resumeLineList[i]];
        }
      })
    }
  }

};

function openResumeAccordion(accordion_element, isOpen) {
  if (isEmpty(accordion_element)) {
    return
  }
  // Set the value to a boolean true if it is 'true', false in all other cases
  const ariaIsTrue = (String(accordion_element.getAttribute('aria-expanded')).toLowerCase() === 'true')
  // console.log(accordion_element.getAttribute('aria-expanded'))
  // Make sure openClose is a bool, and if it is not the correct state, click on the accordion button
  if (typeof isOpen == "boolean" && isOpen != ariaIsTrue) {
    let click_event = new CustomEvent('click');
    accordion_element.dispatchEvent(click_event);
  }
}

function removeResumeFilter() {
  let resume_accordion_list = resumeBlockList;
  let resume_line_list = resumeLineList;

  removeAllHighlightedResumeLines()

  for (let i = 0; i < resume_accordion_list.length; i++) {

    let resume_accordion_summary_button = resume_accordion_list[i].querySelector("[data-type='resume_summary_button']");
    let resume_accordion_detail_button = resume_accordion_list[i].querySelector("[data-type='resume_detail_button']");

    // console.log(resume_line_list);

    openResumeAccordion(resume_accordion_summary_button, true);
    openResumeAccordion(resume_accordion_detail_button, false);

  }
}

function removeAllHighlightedResumeLines() {
  let resume_line_list = resumeLineList;

  for (let i = 0; i < resume_line_list.length; i++) {
    // resume_line_list[i].style.display = 'none';
    resume_line_list[i].classList.remove("add_resume_detail_highlight")
  }
}

function filterResumeItems(filter) { // Modify to allow for multiple filters to be selected and usable

  let activatedFilter = filter.getAttribute("data-filter").toUpperCase();

  // if the button is active, remove it from filter and make it not active
  if (filter.classList.contains('filter-active')) {
    if (activeResumeFilters.indexOf(activatedFilter) > -1) activeResumeFilters.splice(activeResumeFilters.indexOf(activatedFilter),1);
    filter.classList.remove('filter-active');
  } else {
    // Add filter to the fitler list if it's not currently a part of it
    if (activeResumeFilters.indexOf(activatedFilter) === -1) activeResumeFilters.push(activatedFilter);
    filter.classList.add('filter-active');
  }

  // If there are no filters active, show all items and end function
  if (activeResumeFilters.length <= 0) {
    removeResumeFilter()
    return
  }

  // Hide all elements to make only filtered ones appear after
  removeAllHighlightedResumeLines();

  activeResumeFilters.forEach((resume_filter) => {
    // Want live node list in case of dynamic loading
    let filteredResumeBlocks = resumeCategoryElements.resumeBlocks[resume_filter];
    let filteredResumeLines = resumeCategoryElements.resumeLines[resume_filter];

    // Open resume accordionsm
    if (isNotEmpty(filteredResumeBlocks)) {
      filteredResumeBlocks.forEach((resumeBlock) => {
        openResumeAccordion(resumeBlock.querySelector("[data-type='resume_detail_button']"), true);
      }) 
    }

    // Show items
    if (isNotEmpty(filteredResumeLines)) {
      filteredResumeLines.forEach((resumeLine) => {
        // resumeLine.style.display = 'list-item';
        resumeLine.classList.add("add_resume_detail_highlight")
      })
    }

  })

}
