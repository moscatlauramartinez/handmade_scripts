
# Plot one variable
perfil <- function(d, flag, depth, variable){ 
  wrong_value <- -9.99e-29 # SBE puts this value to the wrong data
  clean <- d[d[[flag]] != wrong_value, ] # filter wrong values in tag 
  clean_depth <- clean[clean[[depth]] != wrong_value, ] # filter wrong values in depth
  clean_depth_variable <- clean_depth[clean_depth[[variable]] != wrong_value, ] # filter wrong values in the variable
  
  # plot the graph 
  x <- clean_depth_variable[[variable]]
  y <- clean_depth_variable[[depth]]
  plot(x, y, type = "l", ylim = rev(range(y)),
       xlab = variable, ylab = depth)
  
}

# Plot all the variables given in the dataset
perfiles <- function(data_table, flag = "flag...0.000e.00", depth = "depSM..Depth..salt.water..m...lat...0.00") {
  variables <- colnames(data_table)
  for (variable_perfil in variables) {
    perfil(d, flag, depth, variable_perfil)
    
  }
}


f_path <- "C:/Users/lerin/Desktop/campanya_locate/test2/6_csv_excels/analysis/copia_x_r.cnv"
d <- read.csv(f_path)
perfiles (d)
