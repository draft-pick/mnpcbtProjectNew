$(document).ready(function() {
            $('#carouselBranches').owlCarousel({
                loop:true,
                margin:50,
                nav:false,
                autoplay:true,
                autoplayHoverPause:true,
                smartSpeed:2000,
                autoplayTimeout:4000,
                responsive:{
                    0:{
                        items:1
                    },
                    600:{
                        items:2
                    },
                    1000:{
                        items:3
                    }
                }
            });
        });

$(document).ready(function() {
            $('#carouselReviews').owlCarousel({
                loop:true, //Зацикливаем слайдер
                margin:50, //Отступ от элемента справа в 50px
                nav:true, //Отключение навигации
                autoplay:true, //Автозапуск слайдера
                autoplayHoverPause:true,
                smartSpeed:2000, //Время движения слайда
                autoplayTimeout:8000, //Время смены слайда
                responsive:{ //Адаптивность. Кол-во выводимых элементов при определенной ширине.
                    0:{
                        items:1
                    },
                    600:{
                        items:2
                    },
                    1000:{
                        items:4
                    }
                }
            });
        });

$(document).ready(function() {
            $('#carouselImpLink').owlCarousel({
                loop:true, //Зацикливаем слайдер
                margin:50, //Отступ от элемента справа в 50px
                nav:true, //Отключение навигации
                autoplay:true, //Автозапуск слайдера
                autoplayHoverPause:true,
                smartSpeed:2000, //Время движения слайда
                autoplayTimeout:5000, //Время смены слайда
                responsive:{ //Адаптивность. Кол-во выводимых элементов при определенной ширине.
                    0:{
                        items:2
                    },
                    600:{
                        items:3
                    },
                    1000:{
                        items:5
                    }
                }
            });
        });

$(document).ready(function() {
            $('#carouselManagement').owlCarousel({
                loop:true, //Зацикливаем слайдер
                margin:50, //Отступ от элемента справа в 50px
                nav:true, //Отключение навигации
                autoplay:true, //Автозапуск слайдера
                autoplayHoverPause:true,
                smartSpeed:2000, //Время движения слайда
                autoplayTimeout:5000, //Время смены слайда
                responsive:{ //Адаптивность. Кол-во выводимых элементов при определенной ширине.
                    0:{
                        items:1
                    },
                    600:{
                        items:2
                    },
                    1000:{
                        items:3
                    }
                }
            });
        });

$(document).ready(function() {
            $('#carouselNews').owlCarousel({
                loop:true, //Зацикливаем слайдер
                margin:50, //Отступ от элемента справа в 50px
                nav:true, //Отключение навигации
                autoplay:true, //Автозапуск слайдера
                autoplayHoverPause:true,
                smartSpeed:2000, //Время движения слайда
                autoplayTimeout:5000, //Время смены слайда
                responsive:{ //Адаптивность. Кол-во выводимых элементов при определенной ширине.
                    0:{
                        items:1
                    },
                    600:{
                        items:2
                    },
                    1000:{
                        items:4
                    }
                }
            });
        });



(function($) {
  $.fn.truncate = function(options) {

    var defaults = {
      length: 100,
      minTrail: 10,
      moreText: "",
      lessText: "",
      ellipsisText: ""
    };

    var options = $.extend(defaults, options);

    function find(container, text, minLength) {
      var curIndex = 0;

      for (var nodes = Array.from(container.childNodes); nodes.length;) {
        var node = nodes.shift();
        if (node.nodeType == Node.ELEMENT_NODE) {
          nodes.unshift(...node.childNodes);
          continue;
        }
        var index = -1;
        do {
          index = node.textContent.indexOf(text, index + 1);
        } while (index != -1 && curIndex + index < minLength);

        if (index != -1) {
          curIndex += index;
          return [node, index];
        } else {
          curIndex += node.textContent.length;
        }
      }
      return [null, -1];
    }

    return this.each(function() {
      var obj = $(this);
      var body = this.textContent;

      if (body.length > options.length + options.minTrail) {
        var textToFind = '.';
        if (body.indexOf(textToFind, options.length) != -1) {

          var [node, startIndex] = find(this, textToFind, options.length);
          var splitLocation = startIndex + textToFind.length;

          var str1 = node.textContent.substring(0, splitLocation);
          var str2 = node.textContent.substring(splitLocation + 1);

          node.textContent = str1;

          if (str2.length) {
            $(node).after(`<span  class="truncate_more">${str2}</span>`);
          }

          $(node).after(`<span class="truncate_ellipsis">${options.ellipsisText}</span>`);

          var oi = 0;
          while (node != this) {
            var span = $('<span>').addClass('truncate_more');
            for (var nextNode = node.nextSibling, savedNode; nextNode; nextNode = savedNode) {
              if (nextNode.classList && (nextNode.classList.contains('truncate_more') || nextNode.classList.contains('truncate_ellipsis'))) continue;

              savedNode = nextNode.nextSibling;
              span.append(nextNode);
            }
            node = node.parentNode;
            $(node).append(span);
          }

          obj.find('.truncate_more').css("display", "none");

          obj.append(
            '<div class="clearboth">' +
            '<a href="#" class="truncate_more_link">' + options.moreText + '</a>' +
            '</div>'
          );

          var moreLink = $('.truncate_more_link', obj);
          var moreContent = $('.truncate_more', obj);
          var ellipsis = $('.truncate_ellipsis', obj);
          moreLink.click(function() {
            if (moreLink.text() == options.moreText) {
              moreContent.show('normal');
              moreLink.text(options.lessText);
              ellipsis.css("display", "none");
            } else {
              moreContent.hide('normal');
              moreLink.text(options.moreText);
              ellipsis.css("display", "inline");
            }
            return false;
          });
        }
      }

    });
  };
})(jQuery);

$().ready(function() {
  $('.story').truncate({
    length: 20,
    minTrail: 10,
    moreText: 'Читать полностью',
    lessText: 'Скрыть',
    ellipsisText: "..."
  });
});
