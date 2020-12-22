library(shiny)
library(shinydashboard)

header <- dashboardHeader(disable = T)

sidebar <- dashboardSidebar(disable = T)

body <- dashboardBody(
    fileInput("img", "Choose File", F, "image/*"),
    fluidRow(box(plotOutput("show"), title = "Image Uploaded", width = 6),
    box(plotOutput("show2"), title = "Object Detected", width = 6))
)

dashboardPage(header, sidebar, body)