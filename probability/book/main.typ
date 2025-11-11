#import "@local/dobbikov-book:1.0.0":*

#show: dobbikov.with(
  title: [Measure and Probability Theory],
  subtitle: none,
  author: "Yehor KORORTENKO",
  date: datetime.today(),
  report-style: true
)

#set math.equation(numbering: "(1)")
#toc
// #pagebreak()
#counter(page).update(1)

#include "intro.typ"
// //
#include "ch1-lebesgue.typ"



