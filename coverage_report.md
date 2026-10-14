# Coverage report: microeconomics Anki deck

**Deck file:** `econ_u4_qcaa.csv` | **Cards:** 1110 | **Checklist items:** 157 (all have at least 2 cards) | **Calculation cards:** 0 | **`verify` cards:** 34

**Source:** *Economics for the IB Diploma* (Tragakes, 3rd ed., Cambridge 2020), the trimmed PDF in this repo: Chapters 2-7, book pages 41-245 (PDF page = book page - 40). All page numbers below are **book** page numbers, so you can find them in the printed book or in the PDF's page footers.

## Calls I made

- **Scope.** You asked for everything in the PDF except Theory of Knowledge (TOK) boxes and calculations. The PDF is the whole IB microeconomics unit (Chapters 2-7, SL and HL), so every section is carded, including HL-only sections (behavioural economics, asymmetric information, equity, all of Chapter 7).
- **No calculation cards.** The validation rule 'no formula or worked-number cards' wins over the template's formula/worked-example instructions. So the deck has no MathJax, no formula cards and no worked examples. Formula-only ideas are carded in words where they carry meaning (e.g. 'average revenue is revenue per unit, so it equals price'). Every excluded calculation is listed below.
- **Checklist.** No QCAA checklist came with the request, so the checklist is the textbook's own learning objectives for each section. Where one objective covers several sub-topics (e.g. 'explain the consequences of price controls'), I split it along the book's own sub-headings. Dot-point tags follow the book's numbering: `T4.2.6` = section 4.2, item 6. The generic 'define all the terms' objective is folded into the item each term belongs to. Because the checklist comes from the book, every item has textbook coverage; no item is 'not in textbook'.
- **Header and file name kept exactly as specified** (`#deck:Economics::Unit 4 EA`, `econ_u4_qcaa.csv`), even though the content is microeconomics. Rename the deck in Anki after import if you want (e.g. `Economics::Micro`).
- **Topic tags** are one per textbook section (e.g. `price_controls`, `monopoly`). **Type tags:** the requested `definition`, `chain`, `diagram`, `evaluation` and `verify`, plus four more so every card has a type: `distinguish` (X vs Y), `stakeholders` (effects on groups), `example` and `explain`. `calc` is never used.
- **Australian context.** The book is international, so I added 34 Australian application cards written from my own knowledge, all tagged `verify` (list below). They cover the ACCC and the Competition and Consumer Act, the Fair Work Commission, GST and excise, carbon pricing and the Safeguard Mechanism, Murray-Darling water trading, the PBS, Medicare, HECS-HELP, and similar. They are filed under the dot point they illustrate. Suspend the tag `verify` if you don't want them.
- **Real world focus boxes and examples** in the main text are carded as `example` cards, since EA answers need examples. 'Test your understanding', 'Applying your skills', 'Inquiry and reflection' and exam-style questions add no new content, so they are not carded (the concepts they test are).
- **Australian spelling and terminology** throughout (labour, behaviour, maximise, programs, aluminium, sulfur). Official names keep their own spelling (World Health Organization, OPEC). The validator checks for American spellings.
- **Text extraction.** The PDF has a text layer (pdftotext), so OCR wasn't needed to read it. But the orange key terms on some Chapter 7 pages (e.g. 'market power', 'economies of scale', 'normal profit') were missing from that layer. I OCR'd every page with tesseract (colour-to-black preprocessing) and diffed it against the text layer to recover them. Chapters 2-6 had no missing content.
- **Textbook errors corrected** in the cards (listed at the end) rather than copied.

## Checklist coverage

Each row is one checklist item (a textbook learning objective) with its card count and the textbook pages the cards come from. *AU* means the item also has Australian-context `verify` cards written from my own knowledge. Calculation-only objectives appear as struck-out rows with 0 cards.

### 2.1 Introduction to competitive markets (tag `competitive_markets`, 9 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T2.1.1` | Define a market; local, national and international markets; product and resource markets | 4 | 42 |
| `T2.1.2` | Outline the meaning of a competitive market (competition vs market power) | 5 | 42 |

### 2.2 Demand (tag `demand`, 45 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T2.2.1` | Explain the law of demand (individual demand, ceteris paribus, demand schedule) | 6 | 43-44 |
| `T2.2.2` | Draw a demand curve | 2 | 44 |
| `T2.2.3` | Explain the relationship between individual demand and market demand | 3 | 44-45 |
| `T2.2.4` | Analyse the non-price determinants of demand as causes of demand curve shifts | 16 | 45-46 |
| `T2.2.5` | Using diagrams, distinguish between movements along and shifts of the demand curve | 5 | 47 |
| `T2.2.6` | (HL) Assumptions underlying the law of demand: the law of diminishing marginal utility | 7 | 47-48 |
| `T2.2.7` | (HL) Assumptions underlying the law of demand: the income and substitution effects | 6 | 48-49 |

### 2.3 Supply (tag `supply`, 49 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T2.3.1` | Explain the law of supply (individual supply, supply schedule) | 5 | 49-50 |
| `T2.3.2` | Draw a supply curve (including the vertical supply curve) | 5 | 50-51 |
| `T2.3.3` | Explain the relationship between individual supply and market supply | 2 | 50-51 |
| `T2.3.4` | Analyse the non-price determinants of supply as causes of supply curve shifts | 15 | 51-53 |
| `T2.3.5` | Using diagrams, distinguish between movements along and shifts of the supply curve | 3 | 52-53 |
| `T2.3.6` | (HL) Assumptions underlying the law of supply: the law of diminishing marginal returns | 11 | 54-56 |
| `T2.3.7` | (HL) Assumptions underlying the law of supply: increasing marginal costs and the firm's supply curve | 8 | 55-57 |

### 2.4 Competitive market equilibrium: demand and supply (tag `market_equilibrium`, 25 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T2.4.1` | Draw a diagram to illustrate how demand and supply interact to determine market equilibrium | 10 | 58-59 |
| `T2.4.2` | Analyse demand and supply curve shifts that give rise to a new equilibrium, using excess demand (shortage) and excess supply (surplus) | 5 | 59-60 |
| `T2.4.3` | Draw diagrams to illustrate how shifts in demand and supply give rise to a new equilibrium (incl. free and economic goods) | 10 | 59-61 |

### 2.5 The role of the price mechanism and market efficiency (tag `price_mechanism`, 44 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T2.5.1` | Analyse the price mechanism: resource allocation through the signalling and incentive functions of prices | 9 | 63-64 |
| `T2.5.2` | Analyse the price mechanism: rationing (price and non-price rationing) | 6 | 65 |
| `T2.5.3` | Explain consumer surplus, producer surplus and social (community) surplus (MB and MC interpretation of demand and supply) | 13 | 65-69 |
| `T2.5.4` | Draw a diagram showing maximum social surplus at competitive market equilibrium | 2 | 67-68 |
| `T2.5.5` | Explain the conditions for allocative efficiency at competitive market equilibrium (MB = MC, maximum social surplus) and why intervention may still be needed | 14 | 65-70 |
| - | ~~Calculate consumer and producer surplus from a diagram (AO4)~~ (excluded: calculation) | 0 | 68-69 |

### 2.6 Critique of the maximising behaviour of consumers and producers (HL) (tag `behavioural_economics`, 92 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T2.6.1` | Evaluate the assumptions of consumer rationality, utility maximisation and perfect information | 10 | 72-73, 75 |
| `T2.6.2` | Behavioural critique: biases (rules of thumb, anchoring, framing, availability) | 8 | 73 |
| `T2.6.3` | Behavioural critique: bounded rationality, bounded self-control, bounded selfishness, imperfect information | 7 | 74 |
| `T2.6.4` | Policies inspired by behavioural economics: nudge theory | 12 | 75-76, 83 + AU |
| `T2.6.5` | Policies inspired by behavioural economics: choice architecture (default, restricted and mandated choice) | 13 | 76-78 + AU |
| `T2.6.6` | Evaluate behavioural economics and its policies (mainstream response, advantages, disadvantages) | 15 | 78-79 |
| `T2.6.7` | Business objectives: profit maximisation | 2 | 79 |
| `T2.6.8` | Alternative business objectives: corporate social responsibility, market share, growth, satisficing (and revenue maximisation) | 25 | 79-81 |

### 3.1 Price elasticity of demand (PED) (tag `PED`, 67 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T3.1.1` | Define PED and identify the various degrees and range of values for PED (sign, use of percentages) | 16 | 84-88, 109 |
| `T3.1.2` | Draw diagrams showing the range of values for PED (relatively elastic and inelastic; perfectly elastic, perfectly inelastic, unitary) and PED versus steepness | 7 | 87-89 |
| `T3.1.3` | (HL) Explain and illustrate changing PED along a straight-line downward-sloping demand curve | 5 | 90 |
| `T3.1.4` | Analyse the determinants of PED | 10 | 91-92 |
| `T3.1.5` | Explain the relationship between PED and total revenue | 7 | 92-94 |
| `T3.1.6` | Draw a diagram to show how total revenue changes in response to a price change with elastic, inelastic or unit elastic demand | 4 | 93 |
| `T3.1.7` | Apply PED: its importance for firms (pricing) and government decision-making (indirect taxes) | 5 | 94-95 |
| `T3.1.8` | (HL) Analyse why primary commodities generally have a lower PED than manufactured products (and the consequences for prices and producer revenues) | 13 | 96-97 |
| - | ~~Use the formula for PED to calculate PED, changes in price, changes in quantity and total revenue (AO4)~~ (excluded: calculation) | 0 | 85-87, 93-94 |

### 3.2 Income elasticity of demand (YED) (tag `YED`, 32 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T3.2.1` | Define YED and, depending on the sign of YED, distinguish between normal and inferior goods | 6 | 85, 98-99 |
| `T3.2.2` | Depending on the value of YED (less than or greater than one), distinguish between necessities, luxuries and services | 9 | 99 |
| `T3.2.3` | Draw an Engel curve diagram to show income elastic, income inelastic and inferior goods | 5 | 100-101 |
| `T3.2.4` | (HL) Apply YED: discuss its relevance to firms | 4 | 101-102 |
| `T3.2.5` | (HL) Apply YED: discuss changes in the sectoral structure of an economy | 8 | 102-103 |
| - | ~~Use the formula for YED to calculate YED, change in income and quantity demanded (AO4)~~ (excluded: calculation) | 0 | 98, 100-101 |

### 3.3 Price elasticity of supply (PES) (tag `PES`, 29 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T3.3.1` | Define PES and identify the various degrees and range of values for PES | 10 | 104-106, 110 |
| `T3.3.2` | Draw diagrams showing the range of values for PES (relatively elastic and inelastic; perfectly elastic, perfectly inelastic, unitary) | 6 | 105-106 |
| `T3.3.3` | Analyse the determinants of PES | 6 | 107 |
| `T3.3.4` | (HL) Apply PES: why primary commodities generally have a lower PES than manufactured products (and the consequences) | 7 | 108-109 |
| - | ~~Use the formula for PES to calculate PES, changes in price and changes in quantity (AO4)~~ (excluded: calculation) | 0 | 104 |

### 4.1 Government intervention in markets (tag `govt_intervention`, 20 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T4.1.1` | Outline key reasons why governments intervene in markets (incl. the Real world issue 2 overview) | 17 | 111, 113-114 |
| `T4.1.2` | Outline the forms government intervention takes at the microeconomic level | 3 | 114 |

### 4.2 Price controls (tag `price_controls`, 71 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T4.2.1` | Price controls: meaning, and why they cause persistent market disequilibrium | 3 | 114-115 |
| `T4.2.2` | Price ceilings: explain and draw the consequences for markets (shortage, non-price rationing, underground markets, underallocation, welfare loss) | 12 | 115-117 |
| `T4.2.3` | Price ceilings: consequences for stakeholders and evaluation (incl. rent controls and food price controls) | 15 | 117-118 + AU |
| `T4.2.4` | Price floors for agricultural products: explain and draw the consequences for markets (surplus, government purchases, firm inefficiency, overallocation, welfare loss) | 14 | 120-123 |
| `T4.2.5` | Price floors for agricultural products: consequences for stakeholders and evaluation | 9 | 123, 126 + AU |
| `T4.2.6` | Minimum wages: explain and draw the consequences for the economy and stakeholders, and evaluate | 15 | 125-126 + AU |
| `T4.2.7` | Fixed prices (e.g. event tickets) | 3 | 126 |
| - | ~~(HL) Calculate the effects of price ceilings and price floors on markets and stakeholders (AO4)~~ (excluded: calculation) | 0 | 119-120, 124-125 |

### 4.3 Indirect taxes (tag `indirect_taxes`, 31 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T4.3.1` | The meaning of indirect taxes: excise and general taxes, indirect versus direct, specific versus ad valorem | 8 | 127-128 + AU |
| `T4.3.2` | Indirect taxes and resource allocation; why governments impose indirect taxes | 7 | 127-128 + AU |
| `T4.3.3` | Draw diagrams and explain the impacts of a specific tax on market outcomes | 7 | 128-129, 133 |
| `T4.3.4` | Explain the consequences of indirect taxes for stakeholders | 5 | 129 + AU |
| `T4.3.5` | Evaluate indirect taxes: consumer and producer surplus, welfare loss and allocative inefficiency | 4 | 130 |
| - | ~~(HL) Calculate the effects of indirect taxes on markets and stakeholders (AO4)~~ (excluded: calculation) | 0 | 131-133 |

### 4.4 Subsidies (tag `subsidies`, 29 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T4.4.1` | The meaning of subsidies; subsidies and the allocation of resources | 5 | 134 |
| `T4.4.2` | Why governments grant subsidies (and why subsidies are controversial) | 8 | 134-135 |
| `T4.4.3` | Draw diagrams and explain the impacts of a subsidy on market outcomes | 4 | 135 |
| `T4.4.4` | Explain the consequences of subsidies for stakeholders | 6 | 135-137 |
| `T4.4.5` | Evaluate subsidies: consumer and producer surplus, welfare loss and allocative inefficiency | 6 | 136-138 |
| - | ~~(HL) Calculate the effects of subsidies on markets and stakeholders (AO4)~~ (excluded: calculation) | 0 | 138-140 |

### 5.1 The meaning of common pool resources (tag `common_pool_resources`, 25 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T5.1.1` | Explain the meaning of common pool resources in terms of rivalry and non-excludability | 9 | 144-145 |
| `T5.1.2` | Explain the tragedy of the commons | 3 | 145 |
| `T5.1.3` | Explain the meaning of sustainable and unsustainable production (maximum sustainable yield; renewable and non-renewable resources) | 13 | 145-147 |

### 5.2 Market failure and externalities: diverging private and social benefits and costs (tag `externalities_intro`, 18 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T5.2.1` | Explain market failure as the failure of the market to achieve allocative efficiency | 3 | 147-148 |
| `T5.2.2` | Explain that socially optimum output is produced when MSC = MSB and social surplus is maximum (MPB, MSB, MPC, MSC) | 8 | 148-149 |
| `T5.2.3` | Draw a diagram illustrating allocative efficiency and socially optimum output | 2 | 148-149 |
| `T5.2.4` | Explain the meaning of externalities as an example of market failure | 5 | 148-149 |

### 5.3 Negative production externalities (tag `negative_production_externalities`, 94 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T5.3.1` | Explain negative externalities of production (MSC above MPC) and the resulting overallocation | 7 | 150-151, 161-162 |
| `T5.3.2` | Explain and draw the welfare loss from negative production externalities | 3 | 151 |
| `T5.3.3` | Explain that negative production externalities can illustrate the overuse of common pool resources | 3 | 152 |
| `T5.3.4` | Government responses: indirect (Pigouvian) taxes (explain, diagram) | 5 | 128, 152-153 |
| `T5.3.5` | Government responses: carbon taxes (explain, diagram) | 7 | 153-154 + AU |
| `T5.3.6` | Government responses: tradable permits / cap and trade (explain, diagram) | 9 | 154 + AU |
| `T5.3.7` | Evaluate market-based policies (measurement difficulties, effectiveness, stakeholders; carbon taxes versus tradable permits) | 27 | 154-157 + AU |
| `T5.3.8` | Government responses: legislation and regulation (explain, diagram, evaluate) | 14 | 157-158, 161-162 + AU |
| `T5.3.9` | Government responses: collective self-governance (Ostrom) (explain, evaluate) | 6 | 159-160 |
| `T5.3.10` | Government responses: education and awareness creation (explain, evaluate) | 3 | 159-160 |
| `T5.3.11` | Government responses: international agreements (explain, evaluate) | 10 | 160-161 |
| - | ~~(HL) Calculate welfare loss that arises from negative externalities of production (AO4)~~ (excluded: calculation) | 0 | 151 |

### 5.4 Negative consumption externalities (tag `negative_consumption_externalities`, 34 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T5.4.1` | Explain negative externalities of consumption (MSB below MPB) and the resulting overallocation | 6 | 164-165 |
| `T5.4.2` | Explain and draw the welfare loss from negative consumption externalities | 2 | 165 |
| `T5.4.3` | Negative consumption externalities and the overuse of common pool resources | 3 | 166, 172 |
| `T5.4.4` | Explain the meaning of demerit goods | 2 | 166 |
| `T5.4.5` | Government responses: indirect (Pigouvian) taxes (explain, diagram, evaluate) | 5 | 167 |
| `T5.4.6` | Government responses: legislation and regulation (explain, diagram, evaluate) | 5 | 167-168 + AU |
| `T5.4.7` | Government responses: education and awareness creation (explain, evaluate) | 3 | 168 |
| `T5.4.8` | (HL) Government responses: nudges (explain, evaluate) | 2 | 168-169 |
| `T5.4.9` | Evaluate policies for negative consumption externalities overall (combining policies; sugar taxes) | 6 | 169 + AU |
| - | ~~(HL) Calculate welfare loss that arises from negative externalities of consumption (AO4)~~ (excluded: calculation) | 0 | 165 |

### 6.1 Positive production externalities (tag `positive_production_externalities`, 10 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T6.1.1` | Explain positive externalities of production (MSC below MPC) and the resulting underallocation | 4 | 174 |
| `T6.1.2` | Explain and draw the welfare loss from positive production externalities | 2 | 175 |
| `T6.1.3` | Government responses: direct government provision and subsidies (explain, diagram) | 4 | 176 |
| - | ~~(HL) Calculate welfare loss that arises from positive externalities of production (AO4)~~ (excluded: calculation) | 0 | 175 |

### 6.2 Positive consumption externalities (tag `positive_consumption_externalities`, 43 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T6.2.1` | Explain positive externalities of consumption (MSB above MPB) and the resulting underallocation | 5 | 177-178 |
| `T6.2.2` | Explain and draw the welfare loss from positive consumption externalities | 2 | 178-179 |
| `T6.2.3` | Explain the meaning of merit goods (reasons for underprovision) | 5 | 179 |
| `T6.2.4` | Government responses that raise demand: legislation and regulation, education and awareness creation, nudges (explain, diagram) | 4 | 179-180 + AU |
| `T6.2.5` | Government responses that raise supply: direct government provision and subsidies (explain, diagram) | 7 | 180-181 + AU |
| `T6.2.6` | Evaluate policies to correct positive production and consumption externalities | 9 | 181-182 |
| `T6.2.7` | Summary of externalities and rules for drawing externality diagrams | 11 | 183-184 |
| - | ~~(HL) Calculate welfare loss that arises from positive externalities of consumption (AO4)~~ (excluded: calculation) | 0 | 179 |

### 6.3 Market failure and public goods (tag `public_goods`, 30 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T6.3.1` | Explain public goods as non-rivalrous and non-excludable (and classify private goods, common pool resources, public and quasi-public goods) | 9 | 185-186 + AU |
| `T6.3.2` | Explain the free rider problem and why the market fails to provide public goods | 3 | 185 |
| `T6.3.3` | Evaluate direct government provision of public goods (incl. cost-benefit analysis) | 8 | 186 |
| `T6.3.4` | Evaluate contracting out the provision of public goods to the private sector | 10 | 186-187 |

### 6.4 Asymmetric information (HL) (tag `asymmetric_information`, 37 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T6.4.1` | Explain asymmetric information and distinguish between adverse selection and moral hazard | 6 | 188-190 |
| `T6.4.2` | Adverse selection (sellers know more): evaluate government responses (regulation, provision of information, licensure) | 11 | 188-189 |
| `T6.4.3` | Adverse selection (sellers know more): evaluate private responses (screening and signalling) | 5 | 189 |
| `T6.4.4` | Adverse selection (buyers know more, e.g. health insurance): private and government responses | 9 | 189-190 + AU |
| `T6.4.5` | Moral hazard: examples and responses | 6 | 190-191 |

### 6.5 Equity in the distribution of income and wealth (HL) (tag `equity_distribution`, 15 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T6.5.1` | Explain why the free market results in an unequal distribution of income (equity and equality; factor ownership and factor prices) | 9 | 191-192 + AU |
| `T6.5.2` | Draw a circular flow of income diagram to show why free markets give rise to income inequalities | 2 | 191-192 |
| `T6.5.3` | Explain inequalities in wealth (income versus wealth) and how inequality relates to market failure | 4 | 192-193 |

### 7.1 Introduction to firms, industries and market structures (HL) (tag `market_structures`, 29 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T7.1.1` | Explain the meaning of market power and its link to market failure (firms, industries, market structures) | 10 | 196-197 |
| `T7.1.2` | Explain the main characteristics of perfect competition (many firms, free entry, homogeneous products) | 3 | 197 |
| `T7.1.3` | Explain the main characteristics of monopoly (single or dominant firm, high barriers to entry, no close substitutes) | 4 | 197 |
| `T7.1.4` | Explain the characteristics of imperfect competition: monopolistic competition (many firms, free entry, product differentiation) | 4 | 197 |
| `T7.1.5` | Explain the characteristics of imperfect competition: oligopoly (few large firms, high barriers to entry, interdependence) | 4 | 197 |
| `T7.1.6` | Compare the four market structures (market power versus competition) and explain why perfect competition is studied | 4 | 198 |

### 7.2 Profit maximisation by the rational producer (HL) (tag `costs_revenue_profit`, 34 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T7.2.1` | Explain revenue concepts: total, average and marginal revenue (price takers versus price makers) | 6 | 199-200 |
| `T7.2.2` | Explain cost concepts: economic (explicit and implicit) costs; total, average and marginal cost in the short run | 7 | 201-203 |
| `T7.2.3` | Explain long-run costs: the long-run average cost curve, economies and diseconomies of scale | 9 | 203-204 |
| `T7.2.4` | Explain profit concepts: economic profit, abnormal profit, normal profit, loss | 6 | 204-205, 207 |
| `T7.2.5` | Explain profit maximisation (MR = MC; total revenue minus total cost) | 6 | 205-206 |
| - | ~~(HL) Calculations from data of profit, marginal cost, marginal revenue, average cost, average revenue (AO4)~~ (excluded: calculation) | 0 | 199-206 |

### 7.3 Perfect competition (HL) (tag `perfect_competition`, 29 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T7.3.1` | Explain firms in perfect competition as price takers with no market power (P = D = AR = MR) | 5 | 208-209 |
| `T7.3.2` | Explain and draw short-run profit maximisation (abnormal profit, normal profit, loss) | 5 | 210-211 |
| `T7.3.3` | Explain and draw long-run profit maximisation and equilibrium (normal profit through entry and exit) | 6 | 211-212 |
| `T7.3.4` | Explain allocative efficiency in perfect competition (P = MC, MB = MC, maximum social surplus) | 5 | 213-214 |
| `T7.3.5` | Discuss the advantages and disadvantages of perfect competition | 8 | 214-215 |

### 7.4 Monopoly (HL) (tag `monopoly`, 42 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T7.4.1` | Explain barriers to entry (economies of scale, natural monopoly, branding, legal barriers, control of essential resources, aggressive tactics) | 11 | 215-216 |
| `T7.4.2` | Explain the monopolist's demand and revenue curves and market power (AR above MC; P greater than MC) | 7 | 216-218, 223 |
| `T7.4.3` | Explain and draw profit maximisation by the monopolist (abnormal profit, normal profit, loss) | 4 | 219, 221 |
| `T7.4.4` | Explain and draw natural monopoly | 6 | 219-220 |
| `T7.4.5` | Explain the monopolist's allocative inefficiency and welfare loss compared with perfect competition (higher price, lower output) | 5 | 221-223 |
| `T7.4.6` | Discuss the advantages and disadvantages of monopoly | 9 | 223-224 |

### 7.5 Monopolistic competition (HL) (tag `monopolistic_competition`, 28 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T7.5.1` | Explain the assumptions of monopolistic competition and the methods of product differentiation | 5 | 225 |
| `T7.5.2` | Explain that monopolistic competition has less market power than monopoly (more elastic demand curve); price and non-price competition | 6 | 225-226 |
| `T7.5.3` | Explain and draw profit maximisation in the short run and long run (abnormal profit, normal profit, loss) | 5 | 227-228 |
| `T7.5.4` | Explain allocative inefficiency and market failure; more product variety in exchange for less efficiency | 3 | 228 |
| `T7.5.5` | Discuss the advantages and disadvantages of monopolistic competition (compared with perfect competition and monopoly) | 9 | 228-229 |

### 7.6 Oligopoly (HL) (tag `oligopoly`, 58 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T7.6.1` | Explain the characteristics of oligopoly (few large firms, high barriers to entry, interdependence) | 4 | 230 |
| `T7.6.2` | Explain features of oligopoly: interdependence, strategic behaviour, incentive to collude versus incentive to cheat, risk of price war | 6 | 230-232 |
| `T7.6.3` | Explain the simple game theory payoff matrix (prisoner's dilemma, Nash equilibrium) | 7 | 231-232 |
| `T7.6.4` | Explain the relevance of price and non-price competition in oligopoly | 5 | 232-233 |
| `T7.6.5` | Explain collusive oligopoly and draw a diagram (cartels, difficulties of maintaining them, informal collusion and price leadership) | 14 | 233-234, 236 |
| `T7.6.6` | Distinguish non-collusive oligopoly (strategic behaviour and price rigidity) | 5 | 235 |
| `T7.6.7` | Explain market concentration and concentration ratios (and their weaknesses) | 10 | 235-236 + AU |
| `T7.6.8` | Explain allocative inefficiency and market failure in oligopoly; discuss its advantages and disadvantages | 7 | 237 |

### 7.7 Government intervention in response to abuse of market power (HL) (tag `abuse_of_market_power`, 41 cards)

| Dot point | Checklist item | Cards | Textbook pages |
|---|---|---:|---|
| `T7.7.1` | Discuss advantages of large firms with significant market power (economies of scale, R&D, innovation) and risks to output, price and consumer choice | 5 | 239-240, 243 |
| `T7.7.2` | Explain the meaning of abuse of market power (anti-competitive practices) and where it arises | 5 | 239-240 + AU |
| `T7.7.3` | Evaluate legislation and regulation to protect competition (competition policy, mergers) | 13 | 240-243 + AU |
| `T7.7.4` | Evaluate fines as a response to abuse of market power | 6 | 241, 244 + AU |
| `T7.7.5` | Evaluate government ownership and regulation of natural monopolies (marginal cost and average cost pricing) | 12 | 243-245 + AU |

## Card counts

| Topic tag | Cards |
|---|---:|
| `competitive_markets` | 9 |
| `demand` | 45 |
| `supply` | 49 |
| `market_equilibrium` | 25 |
| `price_mechanism` | 44 |
| `behavioural_economics` | 92 |
| `PED` | 67 |
| `YED` | 32 |
| `PES` | 29 |
| `govt_intervention` | 20 |
| `price_controls` | 71 |
| `indirect_taxes` | 31 |
| `subsidies` | 29 |
| `common_pool_resources` | 25 |
| `externalities_intro` | 18 |
| `negative_production_externalities` | 94 |
| `negative_consumption_externalities` | 34 |
| `positive_production_externalities` | 10 |
| `positive_consumption_externalities` | 43 |
| `public_goods` | 30 |
| `asymmetric_information` | 37 |
| `equity_distribution` | 15 |
| `market_structures` | 29 |
| `costs_revenue_profit` | 34 |
| `perfect_competition` | 29 |
| `monopoly` | 42 |
| `monopolistic_competition` | 28 |
| `oligopoly` | 58 |
| `abuse_of_market_power` | 41 |
| **Total** | **1110** |

| Type tag | Cards |
|---|---:|
| `explain` | 296 |
| `definition` | 232 |
| `example` | 194 |
| `evaluation` | 182 |
| `diagram` | 140 |
| `chain` | 90 |
| `distinguish` | 47 |
| `stakeholders` | 43 |
| `verify` | 34 |
| `calc` | 0 |

A card can carry more than one type tag, so the type counts add up to more than the total.

## `verify` cards (34)

Australian-specific content written from my own knowledge (not in the IB textbook). Check each against current official sources (Fair Work Commission, ATO, ACCC, AER, DCCEEW/Clean Energy Regulator, MDBA, Department of Health, Treasury). Rules and figures change, e.g. merger law changed on 1 January 2026.

| Dot point | Front |
|---|---|
| `T2.6.4` | What is the Australian Government's nudge unit? |
| `T2.6.5` | Does Australia use an opt-in or opt-out (default) system for organ donation, and what does choice architecture suggest about this? |
| `T2.6.5` | How does Australia's superannuation system use default choice? |
| `T4.2.3` | Give an Australian example of a price ceiling in the electricity market. |
| `T4.2.3` | What temporary price ceilings did Australian governments impose on energy in December 2022, and why? |
| `T4.2.5` | What was Australia's Wool Reserve Price Scheme, and why did it collapse? |
| `T4.2.6` | Who sets Australia's national minimum wage, and how? |
| `T4.3.1` | What is Australia's GST, and what kind of indirect tax is it? |
| `T4.3.1` | Give Australian examples of excise taxes that are specific taxes. |
| `T4.3.2` | Give Australian examples of ad valorem taxes on particular goods, including one aimed at luxuries. |
| `T4.3.4` | Why is the GST considered regressive, and how is this reduced? |
| `T5.3.5` | What was Australia's Carbon Pricing Mechanism? |
| `T5.3.6` | What is Australia's Safeguard Mechanism? |
| `T5.3.6` | How does the Murray-Darling Basin use tradable permits to manage a common pool resource? |
| `T5.3.7` | How did Australia's Emissions Reduction Fund ('Direct Action') differ from a carbon tax? |
| `T5.3.8` | How has government regulation and buyback been used to address overuse of water in the Murray-Darling Basin? |
| `T5.3.8` | How are Australian Commonwealth fisheries protected from overfishing with tradable quotas? |
| `T5.4.6` | What tobacco packaging regulation did Australia pioneer, and what kind of policy is it? |
| `T5.4.9` | Does Australia have a tax on sugar-sweetened drinks, and what is used instead? |
| `T6.2.4` | What is Australia's 'No Jab, No Pay' policy, and what type of policy is it? |
| `T6.2.5` | What is the Pharmaceutical Benefits Scheme (PBS)? |
| `T6.2.5` | How does HECS-HELP support the consumption of higher education in Australia? |
| `T6.3.1` | Give Australian examples of public goods provided by government. |
| `T6.4.4` | How does Medicare address adverse selection in Australian health care? |
| `T6.4.4` | What Australian rules counter adverse selection in private health insurance? |
| `T6.5.1` | How is Australia's personal income tax progressive, and how does it promote equity? |
| `T7.6.7` | Give examples of highly concentrated (oligopolistic) markets in Australia. |
| `T7.7.2` | How does Australian law define misuse of market power? |
| `T7.7.3` | What is the ACCC? |
| `T7.7.3` | Which Australian law prohibits cartels and misuse of market power, and how are serious cartels punished? |
| `T7.7.3` | How did Australian merger law change from 1 January 2026? |
| `T7.7.4` | Give an example of a large penalty for cartel conduct in Australia. |
| `T7.7.5` | How does Australia regulate natural monopolies such as electricity networks and broadband? |
| `T7.7.5` | Give examples of privatisation in Australia. |

## IB calculations excluded

Excluded on your instruction (no calculation cards). Conceptual points from these pages, such as what a surplus area represents or what MR = MC means, are still carded.

- p48 (2.2) | Computing marginal utility from total utility (Table 2.2: MU = change in TU)
- p55 (2.3) | Computing marginal product from total product (Table 2.4)
- p56 (2.3) | Computing marginal cost from total cost (Table 2.5)
- p58 (2.4) | Reading/computing the size of shortages and surpluses from demand and supply schedules (Table 2.6)
- p68-69 (2.5) | Calculating consumer surplus, producer surplus and social surplus from a diagram (triangle and trapezium area formulas, P and Q intercepts) - learning objective "calculate consumer and producer surplus from a diagram (AO4)"
- p79 (2.6) | Pizza restaurant profit arithmetic (profit = revenue - costs)
- p80 (2.6) | Market share percentage arithmetic
- p85-87 (3.1) | PED formula; calculating PED, percentage change in price and percentage change in quantity - learning objective 'use the formula for PED to calculate PED, changes in price, changes in quantity and total revenue (AO4)'
- p86 (3.1) | Midpoint (arc) formula for PED (footnote; book says not required)
- p93-94 (3.1) | Calculating total revenue (P x Q) at different points on demand curves and the change in TR
- p98, p100-101 (3.2) | YED formula; calculating YED, percentage change in income and in quantity demanded - learning objective 'use the formula for YED to calculate YED, change in income and quantity demanded (AO4)'; calculating YED from an Engel curve; the 'ratio of slopes' proof of the Engel curve rule
- p104 (3.3) | PES formula; calculating PES, percentage changes in price and quantity supplied - learning objective 'use the formula for PES to calculate PES, changes in price and changes in quantity (AO4)'
- p119-120 (4.2) | HL calculations for a price ceiling: shortage, change in consumer expenditure, change in firm revenue, change in consumer and producer surplus, welfare loss - learning objective 'calculate the effects of price ceilings and price floors on markets and stakeholders (HL only, AO4)'
- p124-125 (4.2) | HL calculations for a price floor: surplus, consumer expenditure, producer revenue, government expenditure, consumer and producer surplus, welfare loss
- p131-133 (4.3) | HL indirect tax calculations: drawing the new supply curve, prices paid and received, consumer expenditure, producer revenue, government revenue, consumer and producer surplus, welfare loss - learning objective 'calculate the effects of indirect taxes on markets and stakeholders (HL only, AO4)'
- p138-140 (4.4) | HL subsidy calculations: new supply curve, prices, consumer expenditure, producer revenue, government expenditure, consumer and producer surplus, welfare loss - learning objective 'calculate the effects of subsidies on markets and stakeholders (HL only, AO4)'
- p151 (5.3) | HL calculation of welfare loss from a negative production externality (triangle area) - learning objective 'calculate welfare loss that arises from negative externalities of production (HL only, AO4)'
- p165 (5.4) | HL calculation of welfare loss from a negative consumption externality - learning objective 'calculate welfare loss that arises from negative externalities of consumption (HL only, AO4)'
- p175 (6.1) | HL calculation of welfare loss from a positive production externality - learning objective 'calculate welfare loss that arises from positive externalities of production (HL only, AO4)'
- p179 (6.2) | HL calculation of welfare loss from a positive consumption externality - learning objective 'calculate welfare loss that arises from positive externalities of consumption (HL only, AO4)'
- p199-206 (7.2) | Calculating total, average and marginal revenue; total, average and marginal cost; profit and the profit-maximising output from tables - learning objective 'calculations from data of profit, marginal cost, marginal revenue, average cost, average revenue (AO4)'
- p210-213 (7.3) | Calculating profit or loss per unit and total profit or loss (P versus AC times Q) and the profit-maximising output from cost tables
- p217-220 (7.4) | Calculating a monopolist's total and marginal revenue, profit-maximising output, price, profit per unit and total profit from tables; numerical marginal revenue example (footnote p218)

## Theory of knowledge boxes excluded

Excluded on your instruction. Some contain evaluation points you might want (noted).

- p71 | Theory of knowledge 2.1: The meaning and implications of maximum social welfare
- p74-75 | Theory of knowledge 2.2: Altruism, perceptions of fairness and self-interested behaviour (homo economicus, Simon, Smith's moral sentiments)
- p82 | Theory of knowledge 2.3: How important are the criticisms of profit maximisation as the firm's main goal? (Friedman vs Samuelson on unrealistic assumptions) - note: contains evaluation points on profit maximisation you may want
- p140-142 | Theory of knowledge 4.1: Allocative efficiency: is it really value-free? (Pareto optimality, Myrdal) - note: this box is the only place Pareto optimality is defined
- p162-164 | Theory of knowledge 5.1: Economic thinking on sustainability and Elinor Ostrom - note: contains Ostrom's policy implication that governments should support local institutions (courts, scientific knowledge) for resource users
- p170-171 | Theory of knowledge 5.2: The ethical dimensions of sustainability and preserving the global climate (polluter pays principle, intergenerational equity)
- p193-194 | Theory of knowledge 6.1: Inequality in relation to market failure (why maximum social surplus is possible with extreme inequality: efficiency counts only demand backed by ability to pay) - note: useful evaluation point
- p238 | Theory of knowledge 7.1: Perfect competition and the real world

## Borderline textbook content

Content that is excluded, partly carded, or not actually in the PDF (the book points to its digital coursebook). Decide whether you want any of it added.

- all sections | Test your understanding questions, Applying your skills questions and exam-style questions - practice questions, no new content (concepts they test are carded)
- p41 | Chapter 2 opener ("Before you start" questions) - no new content
- p49 | Inferior goods and the income/substitution effects (digital coursebook supplementary material, not in the PDF) - not carded
- p56 | Real world focus 2.1 (Ricardo) - carded as one example card plus one evaluation card; the discussion questions themselves are not carded
- p61 | Real world focus 2.2 (avocados; 2018 UK potato crop) - carded as two applied-example cards; the 1982 US avocado oversupply anecdote is not carded separately
- p69 | Footnote: allocative efficiency also answers the 'how to produce' question in the best possible way - the book says the explanation is beyond the syllabus; not carded
- p73 | Footnote 5: how diminishing marginal utility is used to show utility maximisation - beyond the book's scope; not carded
- p81 | Revenue maximisation - the book flags it as 'not in the syllabus' but it is in the PDF, so it is carded (4 cards); suspend them if unwanted
- p83 | Inquiry and reflection questions (chapter 2) - only the definition of 'libertarian paternalism' (Q4) was carded
- p92 | Real world focus 3.1 (lemonade and the diabetic boy) - carded as one example card
- p102 | Real world focus 3.2 (World Bank, demand for rice and wheat) - carded as one example card
- p109-110 | Table 3.4 summary of PED, YED and PES - its examples are carded; the table itself is not
- p110 | Inquiry and reflection questions (chapter 3) - not carded
- p111 | 'Real world issue 2' unit opener (conceptual understandings) - carded under 4.1 (3 cards)
- p118 | Real world focus 4.1 (price controls in Vietnam) - carded as one example card
- p128 | Ad valorem tax diagrams - the book studies only specific taxes, so no ad valorem diagram card
- p133 | Tax incidence and price elasticities of demand and supply - the book points to the digital coursebook (not in the PDF); only the PDF's statement that the burden is shared is carded
- p137-138 | Real world focus 4.2 (US farm subsidies) - carded as two example cards
- p142 | Inquiry and reflection questions (chapter 4) - not carded
- p151-152 | Supplementary material: welfare loss in terms of consumer and producer surplus (area-letter algebra) - not carded
- p156-157 | Real world focus 5.1 (carbon taxes versus tradable permits) - fully carded (evaluation points)
- p161-162 | Real world focus 5.2 (sulfoxaflor and bees) - carded as two example cards
- p165-166 | Supplementary material: welfare loss of a negative consumption externality in terms of consumer and producer surplus - not carded
- p168 | 'A tax on producers or consumers?' - points to the digital coursebook (not in the PDF)
- p169-170 | Real world focus 5.3 (sugar taxes) - carded as three example cards
- p171-172 | Inquiry and reflection (chapter 5) - only Q6's content (air travel emissions, CORSIA) was carded
- p175, p179 | Supplementary material: welfare loss of positive externalities in terms of consumer and producer surplus (area algebra) - not carded
- p182 | Real world focus 6.1 (Bolsa Familia conditional cash transfers) - carded as two cards
- p183 | Table 6.1 summary of externalities - carded as five policy-set cards
- p194 | Inquiry and reflection questions (chapter 6) - not carded
- p212 | Diagrams of the long-run adjustment process in perfect competition - in the digital coursebook (not in the PDF); the process itself is carded
- p235 | Table 7.7 (US concentration ratios) - one example card
- p236 | Real world focus 7.1 (US generic drug price-fixing lawsuit) - carded as one example card
- p240 | Real world focus 7.2 (IMF study on markups) - carded as three cards
- p241-242 | Real world focus 7.3 (Google fine; Obama, Trump, Warren and Cowen quotes) - carded as two cards; the Obama and Trump quotes are not carded
- p243 | Real world focus 7.4 (Asda-Sainsbury's merger) - one card
- p244 | Real world focus 7.5 (EU fines) - three cards
- p244 | Marginal cost pricing diagram for a natural monopoly - in the digital coursebook (not in the PDF)
- p245 | Inquiry and reflection questions (chapter 7) - not carded

## Textbook errors corrected in the cards

- p67 | The book states consumer surplus is "the area under the demand curve and below the price paid". The card uses the standard (correct) wording: under the demand curve and ABOVE the price paid, up to the quantity bought.
- p74 | The book gives Herbert Simon's Nobel Prize year as 1971; it was 1978. The card omits the year.
- p121 | The book's key-point box says a price floor is 'set below the equilibrium price'; the text and diagram (correctly) set it ABOVE equilibrium. Cards use 'above'.
- p160 | The book states the Paris Agreement goal as limiting warming to '1.5%'; the card uses 1.5°C. (The formal goal is to hold warming well below 2°C and pursue efforts to limit it to 1.5°C.)
- p228 | The book says firms in monopolistic competition end up 'earning normal profit where P - MC' (i.e. P = MC); normal profit requires P = AC. Cards use P = AC (with P above MC).

## Validation run before finishing

- CSV re-parsed (skipping the six `#` header lines, which are written verbatim): every row has exactly 3 non-empty fields; row count matches the card sources.
- No duplicate fronts (compared case-insensitively, ignoring HTML and trailing punctuation). I also ran a near-duplicate similarity check by hand and removed 5 overlapping cards; the remaining similar pairs are deliberate mirrors (e.g. elastic vs inelastic, shift left vs right).
- HTML tags balanced, and only simple tags used (`<b>`, `<br>`). No markdown.
- MathJax delimiters balanced (none are used, as there are no calculation cards).
- No `calc` tags, and a pattern check for formulas or worked numbers (`Step 1`, `=` followed by a number, number-operator-number) finds none.
- Every checklist item has at least 2 cards; every card's dot-point tag exists in the checklist.
- Fronts don't refer to 'the text', 'this chapter', page, figure or table numbers.
- Spelling check for American spellings and IB-only terms.
- Every `verify` card is marked as own-knowledge (not attributed to textbook pages).

## Rebuilding

The deck is generated, not hand-edited. Card sources are in `deck_build/cards/*.txt`, the checklist is `deck_build/checklist.txt`, and exclusion notes are in `deck_build/exclusions.md`. Run `python3 deck_build/build.py` (writes and validates the CSV) and then `python3 deck_build/report.py` (writes this report).
