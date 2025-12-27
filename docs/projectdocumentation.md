# Multi-Agent Content Generation System - Project Documentation

## Problem Statement

The task is to design and implement a production-style, multi-agent content generation system that transforms raw product data into structured, machine-readable JSON content. The system must demonstrate true agentic architecture with clear boundaries, single responsibilities, and no shared global state.

## Assumptions

1. **Input Data**: The system receives product data in JSON format with specific fields (product_name, concentration, skin_type, key_ingredients, benefits, how_to_use, side_effects, price).

2. **Output Format**: All outputs must be machine-readable JSON only - no free text, no UI, no HTML.

3. **Product B**: A fictional comparison product (Product B) is defined internally within the ComparisonAgent for comparison purposes.

4. **Deterministic Outputs**: The system should produce consistent, deterministic JSON outputs for the same input data.

5. **No External Dependencies**: The system operates without external APIs, databases, or UI components.

6. **Template System**: Templates define structure, validation rules, and dependencies but contain no business logic.

## Agent Responsibilities

### 1. ProductParserAgent
- **Responsibility**: Parse raw JSON data into validated ProductModel
- **Input**: Raw JSON dictionary
- **Output**: ProductModel instance
- **Key Features**:
  - Validates required fields
  - Normalizes data (strips whitespace, validates types)
  - Raises clear errors for invalid data

### 2. QuestionGeneratorAgent
- **Responsibility**: Generate categorized user questions
- **Input**: ProductModel
- **Output**: Structured JSON with categorized questions
- **Categories**: informational, safety, usage, purchase, comparison
- **Minimum**: 15 questions total across all categories

### 3. BenefitsAgent
- **Responsibility**: Generate structured benefits content
- **Input**: ProductModel
- **Output**: Benefits content block (primary_benefits, benefit_details, key_ingredients_contributing)
- **No Formatting**: Contains only structured data, no template logic

### 4. UsageAgent
- **Responsibility**: Generate structured usage instructions
- **Input**: ProductModel
- **Output**: Usage content block (instructions, frequency, time_of_day, application_steps, precautions, compatible_skin_types)
- **No Formatting**: Contains only structured data, no template logic

### 5. SafetyAgent
- **Responsibility**: Generate structured safety information
- **Input**: ProductModel
- **Output**: Safety content block (side_effects, safety_level, skin_type_compatibility, precautions, when_to_avoid)
- **No Formatting**: Contains only structured data, no template logic

### 6. PriceAgent
- **Responsibility**: Generate structured price information
- **Input**: ProductModel
- **Output**: Price content block (price, currency, price_category, value_assessment, comparison_note)
- **No Formatting**: Contains only structured data, no template logic

### 7. ComparisonAgent
- **Responsibility**: Compare Product A vs Product B
- **Input**: ProductModel (Product A)
- **Output**: Structured comparison block
- **Internal Data**: Defines fictional Product B internally
- **Comparison Points**: price, concentration, ingredients, skin_type_compatibility, benefits, recommendation

### 8. PageAssemblyAgent
- **Responsibility**: Combine templates + content blocks into final JSON pages
- **Input**: Templates, content blocks from logic agents, questions
- **Output**: Complete JSON page structures
- **No Business Logic**: Only assembly and validation, no content generation

## Template System

### Template Components

1. **FAQTemplate**
   - Defines structure for FAQ pages
   - Required fields: product_name, questions, metadata
   - Validation: minimum 15 questions, at least 3 categories

2. **ProductPageTemplate**
   - Defines structure for product pages
   - Required fields: product_name, benefits, usage, safety, price, metadata
   - Dependencies: BenefitsAgent, UsageAgent, SafetyAgent, PriceAgent

3. **ComparisonPageTemplate**
   - Defines structure for comparison pages
   - Required fields: product_a, product_b, comparison_points, recommendation, metadata
   - Validation: both products must have all required fields, at least 3 comparison categories

### Template Principles

- Templates define **structure** (fields, types, rules)
- Templates define **dependencies** (which agents provide data)
- Templates define **validation rules**
- Templates contain **NO business logic**
- Templates contain **NO formatting logic**

## Orchestration Flow

The PipelineOrchestrator controls the execution order and data flow:

```
Step 1: ProductParserAgent
  Input: raw_product_data (dict)
  Output: ProductModel
  Purpose: Parse and validate input data

Step 2: QuestionGeneratorAgent
  Input: ProductModel
  Output: structured_questions
  Purpose: Generate categorized questions

Step 3: Content Logic Agents (Parallel Execution)
  - BenefitsAgent → benefits block
  - UsageAgent → usage block
  - SafetyAgent → safety block
  - PriceAgent → price block
  Input: ProductModel (each agent)
  Output: content_blocks (dict)

Step 4: ComparisonAgent
  Input: ProductModel
  Output: comparison_data
  Purpose: Compare Product A vs Product B

Step 5: PageAssemblyAgent
  Input: templates + content_blocks + questions
  Output: complete_pages (dict)
  Purpose: Assemble final JSON structures

Step 6: Save Outputs
  Input: complete_pages
  Output: JSON files (faq.json, product_page.json, comparison_page.json)
  Location: outputs/ directory
```

## Data Flow Explanation

### Data Flow Diagram

```
raw_product_data (JSON)
    ↓
ProductParserAgent
    ↓
ProductModel (normalized, validated)
    ├──→ QuestionGeneratorAgent → structured_questions
    ├──→ BenefitsAgent → benefits_block
    ├──→ UsageAgent → usage_block
    ├──→ SafetyAgent → safety_block
    ├──→ PriceAgent → price_block
    └──→ ComparisonAgent → comparison_data
            ↓
    PageAssemblyAgent
    ├──→ FAQ Page (questions)
    ├──→ Product Page (benefits + usage + safety + price)
    └──→ Comparison Page (comparison_data)
            ↓
    JSON Files (outputs/)
```

### Key Data Flow Principles

1. **Single Source of Truth**: ProductModel is the single source of truth for product data
2. **No Shared State**: Each agent receives data as input and produces output - no global state
3. **Explicit Dependencies**: Templates explicitly define which agents provide which data
4. **Immutable Data**: ProductModel is created once and passed to agents (not modified)
5. **Clear Boundaries**: Each agent has explicit inputs and outputs with no side effects

## Why This is NOT a Monolithic System

### 1. **Agent Separation**
- Each agent is a separate Python module/class
- Agents have single, well-defined responsibilities
- Agents can be tested, modified, or replaced independently

### 2. **No Shared Global State**
- Each agent receives data as function parameters
- No global variables or shared mutable state
- Data flows explicitly through function calls

### 3. **Template System Independence**
- Templates are separate from agents
- Templates define structure, not logic
- Templates can be modified without changing agents

### 4. **Orchestrator as Controller**
- Orchestrator controls flow but contains no business logic
- Orchestrator coordinates agents but doesn't generate content
- Orchestrator can be modified to change execution order without affecting agents

### 5. **Modular Architecture**
- Each component (agent, model, template) is in its own module
- Clear separation of concerns
- Easy to extend with new agents or templates

### 6. **Explicit Dependencies**
- Each agent's dependencies are explicit in its constructor or method signatures
- No hidden dependencies or magic
- Easy to understand data flow

### 7. **Single Responsibility Principle**
- ProductParserAgent: Only parsing
- QuestionGeneratorAgent: Only question generation
- Content Agents: Only their specific content type
- PageAssemblyAgent: Only assembly, no generation
- Orchestrator: Only coordination, no content

### 8. **Testability**
- Each agent can be tested independently
- Mock data can be passed to any agent
- No need to set up entire system for unit tests

## Project Structure

```
Multi-Agent/
├── agents/
│   ├── __init__.py
│   ├── product_parser_agent.py
│   ├── question_generator_agent.py
│   ├── benefits_agent.py
│   ├── usage_agent.py
│   ├── safety_agent.py
│   ├── price_agent.py
│   ├── comparison_agent.py
│   └── page_assembly_agent.py
├── models/
│   ├── __init__.py
│   └── product_model.py
├── templates/
│   ├── __init__.py
│   ├── faq_template.py
│   ├── product_page_template.py
│   └── comparison_page_template.py
├── orchestrator/
│   ├── __init__.py
│   └── pipeline_orchestrator.py
├── data/
│   └── product_data.json
├── outputs/
│   ├── faq.json
│   ├── product_page.json
│   └── comparison_page.json
├── docs/
│   └── projectdocumentation.md
└── main.py
```

## Output Files

### outputs/faq.json
- Contains categorized questions generated by QuestionGeneratorAgent
- Validated against FAQTemplate
- Structure: product_name, questions (with categories), metadata

### outputs/product_page.json
- Contains complete product information
- Combines content from BenefitsAgent, UsageAgent, SafetyAgent, PriceAgent
- Validated against ProductPageTemplate
- Structure: product_name, benefits, usage, safety, price, metadata

### outputs/comparison_page.json
- Contains comparison between Product A and Product B
- Generated by ComparisonAgent
- Validated against ComparisonPageTemplate
- Structure: product_a, product_b, comparison_points, recommendation, metadata

## Execution

Run the system using:
```bash
python main.py
```

The system will:
1. Load product data from `data/product_data.json`
2. Execute the multi-agent pipeline
3. Generate three JSON files in `outputs/` directory
4. Print execution summary

## Extensibility

The system is designed for easy extension:

1. **New Agents**: Add new agent classes following the same pattern
2. **New Templates**: Define new templates with structure and validation
3. **New Content Types**: Add new content logic agents
4. **Pipeline Modifications**: Modify orchestrator to change execution flow
5. **New Output Formats**: Extend PageAssemblyAgent to support new page types

All extensions maintain the agentic architecture principles: single responsibility, explicit inputs/outputs, no shared state.


