;; --- KNOWLEDGE BASE ---
!(bind! &beliefs (new-space))
!(add-atom &beliefs (Belief Visual 1 1))
!(add-atom &beliefs (Belief Symbolic 1 1))
!(add-atom &beliefs (Belief Analogy 1 1))

;; --- UPDATE RULE ---
(= (update-belief $style $success)
   (match &beliefs (Belief $style $a $b)
          (let () (remove-atom &beliefs (Belief $style $a $b))
                  (if (== $success 1)
                      (add-atom &beliefs (Belief $style (+ $a 1) $b))
                      (add-atom &beliefs (Belief $style $a (+ $b 1)))))))