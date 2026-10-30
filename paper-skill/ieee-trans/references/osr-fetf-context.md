# OSR-FETF Project Context

Read this file only for OSR-FETF. It records project-specific context, not a default topic or architecture for future papers. Verify current implementation and evidence before using any scientific claim. General style and structure belong in user-style-profile.md and abstract-introduction-outline.md.

## Innovation Narrative for the Current ETF Method

- Position OSR-FETF as open-set RF fingerprinting for previously unseen clients using federated representation learning. Avoid “个性化” or “personalized” when naming this method or its task. Frame the Abstract and Introduction around knowledge reuse across clients and local open-set adaptation, not receiver conditions, receiver mismatch, or cross-receiver transfer. Federated training is the means of learning a reusable encoder, not the open-set task itself. Do not silently change the formal protocol or experimentally grounded client definitions when changing this narrative. Do not describe this as a shared global identity classifier. Preserve the terminology of other methods when discussing prior work.
- When using the user's phrase “客户端内的强收敛需求”, explain it through class-compact and class-separated features. Do not reinterpret it as a proved faster optimization rate, global convergence, or guaranteed unknown-device rejection.
- Frame the method as a global-guided, hierarchical ETF geometric construction rather than a combination of ETF, projection, neural collapse, and KNN modules.
- Present the central tension as two different representation goals. The global ETF supports consistent shared-encoder updates for federated aggregation, while client strong neural collapse provides the compact and separated local structure needed for client open-set recognition. Do not motivate the client ETF primarily through local class-count matching or the limitation of direct row selection.
- The causal spine is:
  1. Training clients use a fixed global ETF with pre-projector auxiliary supervision to provide a common optimization reference for the shared encoder and improve the consistency of client update directions during FedAvg.
  2. The aggregated shared encoder serves the participating clients and transfers the knowledge learned from them to a new evaluation client.
  3. Each participating or new client uses its local known samples and private projector to form strong neural collapse for local discrimination and rejection. A new client performs local adaptation after receiving the shared encoder.
  4. A client ETF constructed inside the subspace spanned by the global ETF provides this local structure while constraining it to the global ETF row subspace.
  5. The adapted projected features are used to fit client-local class-conditional and background statistics, and the relative Mahalanobis distance score provides the final open-set decision.
- Foreground the most distinctive technical action: client ETF reconstruction constrained by the global ETF subspace. Present the global ETF both as an aggregation-alignment anchor and as the geometric basis from which client ETF structures are derived.
- State the unifying contribution as jointly supporting federated parameter aggregation and client open-set recognition through global auxiliary supervision and local ETF reconstruction within the global subspace.

## Technical Claim Guardrails

- The global ETF is maximally separated for the full global class count. The limitation is that a client-specific row selection generally does not form the maximum-separation simplex for the client's class count.
- Constructing a client ETF inside the global ETF subspace establishes geometric inheritance and restricts arbitrary local orientation. By itself, it does not guarantee identical shared-encoder gradients when the main loss backpropagates through a private projector.
- The global auxiliary branch is the primary direct mechanism for shared-encoder alignment. The main projected loss may still backpropagate through the shared encoder, so describe the two branches as functionally differentiated but computationally coupled.
- ETF heads are fixed buffers rather than learned classifier weights. Prefer “构建”, “重构”, “约束”, or “几何机制” over wording that implies the ETF matrices themselves are trained.
- Treat the private projector and client-local RMDS statistics as essential parts of the training/inference loop, but do not present RMDS alone as the principal methodological novelty.
- Open-set separation is conditional on compact known-class features and distributional separation. Avoid universal rejection guarantees.
- For the current RF open-set paper, make the main comparison table center on AUROC, FPR95, AUPR-IN, and AUPR-OUT for every client. Do not use known-class accuracy as the main cross-method comparison unless the user asks for it.
- State each baseline's OOD scoring or post-hoc rule explicitly, such as MSP, energy, kNN, or a method-native score. Select the rule from the method definition or a validation-only protocol, never because its test result is weaker than the proposed method. When detector choice materially changes the conclusion, report a detector-controlled comparison or the relevant alternatives.

## Project-Specific Terminology

- Use “开集识别”, not “开放集识别”. Avoid calling this method “个性化” or “联邦开集识别”. Federated representation learning is its training means.
- Say “客户端 ETF”, not “严格客户端 ETF”. Do not foreground partially overlapping class sets unless essential to the claim or protocol.
- Describe the actual operation, “在全局 ETF 子空间内重构客户端 ETF”, rather than labeling the innovation “具有继承关系”.
- Avoid coordinate-system rhetoric. Use precise terms such as shared-feature supervision, common training reference, global ETF subspace, and update-direction consistency. Do not claim identical client gradients.