#Oppgave 1a
x = read.table("https://www.uio.no/studier/emner/matnat/math/STK1110/data/forsikringskrav.txt", header=F)[,1]

n = length(x)
mean(x)
var(x)

# Moment-estimatorene for alpha og gamma
gamma.mom = mean(x)/var(x)
alpha.mom = mean(x) * gamma.mom

alpha.mom
gamma.mom

# Oppgave 1b
loglik = n * alpha.mom * log(gamma.mom) -
  n * lgamma(alpha.mom) +
  (alpha.mom - 1) * sum(log(x)) -
  gamma.mom * sum(x)

loglik

# Oppgave 1d
negloglikgamma = function(logalpha,x=x)
{
  n = length(x)
  alpha=exp(logalpha)
  gamma = alpha/mean(x)
  logL = n*alpha*log(gamma)-n*lgamma(alpha)+
    (alpha-1)*sum(log(x))-gamma*sum(x)
  -logL
}

fit.ml=optim(log(alpha.mom),negloglikgamma,x=x,method="BFGS")
fit.ml

# ML-estimatorene for alpha og gamma
alpha.ml = exp(fit.ml$par)
gamma.ml = alpha.ml / mean(x)

alpha.ml
gamma.ml

# Oppgave 1e
B = 1000
alpha.boot = numeric(B)
gamma.boot = numeric(B)

for (b in 1:B) {
  # Trekk et bootstrap-datasett
  x.boot = sample(x, size = length(x), replace = T)
  
  # Finn ML-estimatet
  fit.boot = optim(log(alpha.ml), negloglikgamma, x = x.boot, method = "BFGS")
  
  # Lagre estimatet for alpha og gamma
  alpha.boot[b] = exp(fit.boot$par)
  gamma.boot[b] = alpha.boot / mean(x.boot)
}

# Estimering av standardavviket til bootstrap-estimatene
sd(alpha.boot)
sd(gamma.boot)

# 95% konfidens-intervaller for alpha og gamma
quantile(alpha.boot, c(0.025, 0.975))
quantile(gamma.boot, c(0.025, 0.975))

# Oppgave 1f

# mu = alpha / gamma
mu.boot = alpha.boot / gamma.boot

# 95% konfidens-intervall for mu
quantile(mu.boot, c(0.025, 0.975))

# 99% konfidens-intervall for mu
quantile(mu.boot, c(0.005, 0.995))

# Oppgave 2a
x = c(525, 587, 547, 558, 591, 531, 571, 551, 566, 622, 561, 502, 556, 565, 562)
n = length(x)

#t-verdien for 95% konfidensintervall
t = qt(0.975, df = n-1)

# Standardfeilen til gjennomsnittet
SE = sd(x)/sqrt(n)

# Feilmarginen
fm = t * SE

#??vre og nedre grense av intervallet
??vre = mean(x) + fm
nedre = mean(x) - fm

# Oppgave 2b
B = 10000
nedre = numeric(B)
??vre = numeric(B)

# Simulasjon for 10 000 datasett
for (i in 1:B) {
  x = rnorm(15, mean = 558, sd = 30)
  
  x.bar = mean(x)
  s = sd(x)
  SE = s/sqrt(15)
  
  t = qt(0.975, df = 14)
  
  # Finn ??vre og nedre grense for intervallene
  ??vre[i] = x.bar + t*SE
  nedre[i] = x.bar - t*SE
}

# Intervallet inneholder mu = 558 
inneholder = (nedre <= 558) & (??vre >= 558)
mean(inneholder)

# Oppgave 2c
B = 10000
nedre.c = numeric(B)
??vre.c = numeric(B)

# Simulasjon for 10 000 datasett
for (i in 1:B) {
  x = rnorm(15, mean = 558, sd = 30)
  
  x.bar = mean(x)
  s = sd(x)
  SE = s/sqrt(15)
  
  # Finn ??vre og nedre grense for intervallene
  ??vre.c[i] = x.bar + 1.96*SE
  nedre.c[i] = x.bar - 1.96*SE
}

# Intervallet inneholder mu = 558 
inneholder.c = (nedre.c <= 558) & (??vre.c >= 558)
mean(inneholder.c)

# Oppgave 2d
chi.nedre = qchisq(0.025, df = 14)
chi.??vre = qchisq(0.975, df = 14)

B = 10000
nedre.sigma = numeric(B)
??vre.sigma = numeric(B)

# Simulasjon for 10 000 datasett
for (i in 1:B) {
  x = rnorm(15, mean = 558, sd = 30)
  s = sd(x)
  
  # Finn ??vre og nedre grense for intervallene
  ??vre.sigma[i] = s*(sqrt((n-1)/chi.nedre))
  nedre.sigma[i] = s*(sqrt((n-1)/chi.??vre))
}

# Intervallet inneholder sigma = 30 
inneholder.sigma = (nedre.sigma <= 30) & (??vre.sigma >= 30)
mean(inneholder.sigma)

# Oppgave 2e
B = 10000
nedre = numeric(B)
??vre = numeric(B)

# Simulasjon for 10 000 datasett
for (i in 1:B) {
  z = rt(15, df = 7)
  x = 558 + 30*z
  
  x.bar = mean(x)
  s = sd(x)
  SE = s/sqrt(15)
  
  t = qt(0.975, df = 14)
  
  # Finn ??vre og nedre grense for intervallene
  ??vre[i] = x.bar + t*SE
  nedre[i] = x.bar - t*SE
}

# Intervallet inneholder mu = 558 
inneholder = (nedre <= 558) & (??vre >= 558)
mean(inneholder)

# Oppgave 2f
chi.nedre = qchisq(0.025, df = 14)
chi.??vre = qchisq(0.975, df = 14)

B = 10000
nedre.sigma = numeric(B)
??vre.sigma = numeric(B)

# Det faktiske standardavviket til X
sigma.tilde = 30*sqrt(1.4)

# Simulasjon for 10 000 datasett
for (i in 1:B) {
  z = rt(15, df = 7)
  x = 558 + 30*z
  s = sd(x)
  
  # Finn ??vre og nedre grense for intervallene
  ??vre.sigma[i] = s*(sqrt((n-1)/chi.nedre))
  nedre.sigma[i] = s*(sqrt((n-1)/chi.??vre))
}

inneholder = (nedre.sigma <= sigma.tilde) & (??vre.sigma >= sigma.tilde)
mean(inneholder)