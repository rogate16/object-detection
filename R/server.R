library(shiny)

shinyServer(function(input, output) {
  

    output$show <- renderPlot({
        
        if(is.null(input$img)){
          img <- imager::load.image("google.png")
        } else {
          img <- imager::load.image(input$img$datapath)
        }
        par(mar = c(0.5, 0, 0.5, 0))
        plot(img, axes=F, ann=F)
        
    })
    
    output$show2 <- renderPlot({
        
        if(is.null(input$img)){
          detected <- imager::load.image("google_det.png")  
        } else {
          image_darknet_detect(input$img$datapath, yolo, 0.2)
          detected <- imager::load.image("predictions.png")
        }
        par(mar = c(0.5, 0, 0.5, 0))
        plot(detected, axes=F, ann=F)
        
    })
    
})
