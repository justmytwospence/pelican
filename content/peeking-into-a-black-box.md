title: Peeking into a black box
date: 2013-10-22 23:59
tags: R, Shiny, stepwise

I’ve been meaning to try my hand at Shiny for a while now, and I’ve finally gotten around to it. Shiny is an R package from the people who brought you RStudio that allows you to take R code and embed it within an interactive HTML UI that uses Bootstrap styling. You can get surprising mileage out of R visualization when it magically animates (I would have named the package “pinocchio” but they didn’t ask me). [Check out the Shiny showcase if you don’t believe me.][]  

My original idea to get my feet wet was a real-time visualization of least-angle regression, because I’m fascinated by how it turns a discrete algorithm like step-wise regression into an analogue algorithm (or at least an approximation of one). I think it would be neat to watch this analogue “dialing in” of regression coefficients.  

Making that happen would require ripping apart the code in the LARS package. I wasn’t feeling quite that ambitious considering a few other looming assignments, but the fact that its even an option for me to explore in the future is one of the beautiful features of an open source language like R. Ultimately I settled on visualizing a plain vanilla forward stepwise regression, because I had a home-brew implementation lying around from a previous assignment.  

Without further ado, here’s a preview in .gif format:  

![Step-lively, now!]({filename}/images/steplively.gif)  

You can run the actual app for yourself in your R console with only three lines of code (two if you already have shiny installed!)

```r
install.packages('shiny')
library(shiny)
runGitHub('shiny_stepwise', 'justmytwospence')
```

The ability to run anyone’s shiny app straight from their GitHub profile is super cool. You can see the source code on my GitHub as well. Once I hear back from the RStudio folks about getting in on the beta version of their web hosting service, I can try to make it available to people who don’t have R installed (but really, will anyone who cares about stepwise regression *not* have R installed?).  

I think its actually a pretty cool glimpse into an algorithm that is (justifiably) distrusted by many for being too opaque. I’ll continue adding functionality and hopefully it will useful for someone other than myself in the not too distant future; either as a simple learning demonstration or maybe even in an actual modeling context. I will definitely be making more Shiny apps in the future as I become more familiar with its advanced features. Building dashboards, as I am discovering, can be quite addicting.  

EDIT: The app is now live! See it at [steplively.spencerboucher.com][]

  [Check out the Shiny showcase if you don’t believe me.]: http://www.rstudio.com/shiny/showcase/
  []: http://media.tumblr.com/66066fffc66745aa8b9047b5e49032d3/tumblr_inline_mv3h49xMTG1r0kwho.gif
  [steplively.spencerboucher.com]: http://steplively.spencerboucher.com
