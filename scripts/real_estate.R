#written by : Stefan Solagratio Simanjuntak/1039092

library(faraway)

data <- read.csv(
  file = 'generic-real-estate-consulting-project-group-0/notebooks/final.csv')

# Plotting Interactions

par(mfrow=c(2,2))

with(data, interaction.plot(prev_year, type_1, log(rent_pw/rent_yminthree)));
with(data, interaction.plot(prev_year, car, log(rent_pw/rent_yminthree)));
with(data, interaction.plot(prev_year, bath, log(rent_pw/rent_yminthree)));
with(data, interaction.plot(prev_year, bed, log(rent_pw/rent_yminthree)));

par(mfrow=c(1,2))
with(data, interaction.plot(train_duration_min, prev_year, log(rent_pw/rent_yminthree)));
with(data, interaction.plot(train_distance_m, prev_year, log(rent_pw/rent_yminthree)));

par(mfrow=c(2,2))
with(data, interaction.plot(type_1, car, log(rent_pw/rent_yminthree)));
with(data, interaction.plot(type_1, bath, log(rent_pw/rent_yminthree)));
with(data, interaction.plot(type_1, bed, log(rent_pw/rent_yminthree)));
with(data, interaction.plot(train_duration_min,type_1, log(rent_pw/rent_yminthree)));

par(mfrow=c(1,1))
with(data, interaction.plot(train_distance_m,type_1, log(rent_pw/rent_yminthree)));

par(mfrow=c(2,2))
with(data, interaction.plot(car, bath, log(rent_pw/rent_yminthree)));
with(data, interaction.plot(car, bed, log(rent_pw/rent_yminthree)));
with(data, interaction.plot(train_duration_min,car, log(rent_pw/rent_yminthree)));
with(data, interaction.plot(train_distance_m,car, log(rent_pw/rent_yminthree)));

par(mfrow=c(1,3))
with(data, interaction.plot(bath, bed, log(rent_pw/rent_yminthree)));
with(data, interaction.plot(train_duration_min,bath, log(rent_pw/rent_yminthree)));
with(data, interaction.plot(train_distance_m,bath, log(rent_pw/rent_yminthree)));

par(mfrow=c(1,2))
with(data, interaction.plot(train_duration_min,bed, log(rent_pw/rent_yminthree)));
with(data, interaction.plot(train_distance_m,bed, log(rent_pw/rent_yminthree)));

# The base model

model <- lm(rent_pw ~ offset(log(rent_yminthree)) + 
              (prev_year+car + bath + bed + train_duration_min + train_distance_m)^2
                 ,data=data);

# Feature Selection

mod2 <- step(model, scope=~.,trace = FALSE)
summary(mod2)

# Contrast with Anova test

anova(model, test="Chi")

# Diagnostic Plot

par(mfrow = c(2, 2))
plot(mod2)