;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname oblig2b-anamji-alekskir) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; anamji & alekskir

;; OPPGAVE 1

;; a)
(define (make-counter)
    (let ((count 0))
      (lambda ()
        (set! count (+ count 1))
        count)))

;; Kjøreeksempler 
(define count 42)
(define c1 (make-counter))
(define c2 (make-counter))
(c1) ;; -> 1
(c1) ;; -> 2
(c1) ;; -> 3
count ;; -> 42
(c2) ;; -> 1