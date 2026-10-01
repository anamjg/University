(load "evaluator.scm")

;;Oppgave 1
;;a)

(set! the-global-environment (setup-environment))
(mc-eval '(+ 1 2) the-global-environment)

;;(read-eval-print-loop)

(define (foo cond else)
  (cond ((= cond 2) 0)
        (else (else cond))))

(define cond 3) ;;ok
(define (else x) (/ x 2)) ;;ok
(define (square x) (* x x)) ;;ok


(foo 2 square) ;; 0 
(foo 4 square) ;;16
(cond ((= cond 2) 0)
      (else (else 4))) ;; 2