# DESIGN_DOCUMENT.md

# Laya Africa Evaluation Suite - Design Document

## 1. Original Architecture

The original [laya System-1 decision engine](https://github.com/NandhaKishorM/laya) is a non-autoregressive transformer-based model that provides:
- Typed choice, score, and yes/no decisions over any text
- Support for 100+ languages through a router that selects appropriate checkpoints
- Single forward pass inference for efficiency
- Apache-2.0 licensed open-source model

## 2. Problems Identified

Through analysis of the laya project and documentation, the following gaps were identified:

### 2.1 Language Coverage Gaps
- Limited evaluation data for African languages despite laya's claimed 100+ language support
- No specific benchmarks for Swahili, Luganda, Amharic, Hausa, Yoruba in decision-making contexts
- Lack of code-switching evaluation data common in African linguistic contexts

### 2.2 Security Evaluation Gaps
- No standardized prompt injection robustness testing suite
- Limited security evaluation beyond basic functionality
- No African-language specific adversarial testing

### 2.3 Evaluation Infrastructure Gaps
- No purpose-built evaluation runners for rapid iteration
- Missing mock data fixtures for CI/CD integration
- Lack of comprehensive reporting tools

## 3. Proposed Architecture

The Laya Africa Evaluation Suite introduces three complementary components:

### 3.1 African-Language Triage Dataset Component
- **Purpose**: Provide standardized benchmarks for African language performance
- **Structure**: JSONL datasets organized by language and domain
- **Languages**: Swahili (sw), Luganda (lug), Amharic (am), Hausa (ha), Yoruba (yo), English control (en), Code-switch (sw-en)
- **Domains**: Healthcare, social services, finance, communications, emergency

### 3.2 Prompt-Injection Guard Robustness Harness Component
- **Purpose**: Evaluate security of laya deployments against prompt injection
- **Structure**: Python package with extensible test case framework
- **Injection Types**: Direct, indirect, role-play, context-ignore, length-based, encoding
- **Severity Levels**: Low, medium, high
- **Reporting**: Detailed accuracy metrics by type and severity

### 3.3 Evaluation Runners Component
- **Purpose**: Enable efficient testing with both mock and live models
- **MockRunner**: Fast, deterministic testing using precomputed results
- **LiveCheckpointRunner**: Integration with actual laya model checkpoints
- **Unified Interface**: Consistent API for both evaluation modes

## 4. New Architecture

### 4.1 Component Interaction
```
User Application
        ↓
[Evaluation Interface] ←→ [Dataset Loader]
        ↓
[Runner Selection] → [MockRunner OR LiveCheckpointRunner]
        ↓
[Prediction Collection] → [Results Aggregator]
        ↓
[Metrics Calculator] → [Report Generator]
        ↓
[Security Evaluation] ←→ [Guard Harness]
        ↓
[Final Report]
```

### 4.2 Data Flow
1. Dataset loader reads JSONL files from `datasets/`
2. Runner selects evaluation mode (mock/live)
3. For each example:
   - Text preprocessing (language detection, normalization)
   - Model inference (mock or live)
   - Post-processing (triage category extraction)
   - Result storage
4. Metrics calculator computes accuracy, precision, recall by language/domain
5. Guard harness runs security evaluation if requested
6. Report generator creates JSON and human-readable reports

### 4.3 Interface Design
- **Evaluation Protocol**: Standardized input/output format
- **Plugin Architecture**: Easy to add new languages/domains
- **Extension Points**: Custom injection types, severity levels
- **Configuration**: YAML-based configuration for evaluation parameters

## 5. Technology Decisions

### 5.1 Language Choice (Python)
- **Reasoning**: laya is primarily accessed via Python bindings
- **Benefits**: Rich NLP ecosystem, easy integration with ML tools
- **Alternatives Considered**: Rust (performance), JavaScript (web integration)
- **Decision**: Python for maximum compatibility with laya ecosystem

### 5.2 Data Format (JSONL)
- **Reasoning**: Simple, streaming-friendly, widely supported
- **Benefits**: Easy to generate, parse, and process
- **Alternatives Considered**: CSV, Parquet, SQLite
- **Decision**: JSONL for simplicity and compatibility

### 5.3 Package Structure
- **Reasoning**: Modular, extensible, follows Python best practices
- **Benefits**: Easy to install, test, and maintain
- **Alternatives Considered**: Monolithic script, Jupyter notebook
- **Decision**: Proper Python package for professional distribution

## 6. Security Decisions

### 6.1 Input Validation
- All dataset inputs validated for JSONL format
- Text inputs sanitized where appropriate
- No execution of untrusted code

### 6.2 Secure Defaults
- Mock runner uses deterministic simulated data
- Live runner requires explicit checkpoint loading
- No automatic model downloading from untrusted sources

### 6.3 Dependency Security
- Dependencies pinned to known-good versions
- Regular vulnerability scanning recommended
- SBOM generation for supply chain security

## 7. Performance Decisions

### 7.1 Mock Runner Optimization
- Precomputed results eliminate model inference latency
- Memory-efficient streaming of large datasets
- Deterministic output for reproducible testing

### 7.2 Live Checkpoint Runner
- Lazy model loading to minimize memory footprint
- Batch processing where supported by laya
- Progress reporting for long-running evaluations

### 7.3 Reporting Efficiency
- Incremental report generation to avoid memory spikes
- Optional detailed result storage
- Summary statistics for quick overview

## 8. Scalability Considerations

### 8.1 Horizontal Scaling
- Dataset sharding for parallel evaluation
- Independent language/domain evaluation
- Map-reduce compatible for cluster deployment

### 8.2 Vertical Scaling
- Configurable batch sizes for memory-constrained environments
- Streaming processing for arbitrarily large datasets
- Optional GPU acceleration for live runner

### 8.3 Language Expansion
- Simple JSONL format for easy community contributions
- Standardized metadata schema for consistency
- Clear contribution guidelines for new languages

## 9. Deployment Architecture

### 9.1 Local Development
- Python virtual environment or conda environment
- Optional Docker container for consistent environment
- Pre-commit hooks for code quality

### 9.2 CI/CD Integration
- Mock runner suitable for GitHub Actions
- Artifact storage for evaluation results
- Badge generation for README visibility

### 9.3 Production Deployment
- Containerized deployment options
- API wrapper for service-oriented architectures
- Monitoring and alerting integrations

## 10. Testing Strategy

### 10.1 Unit Testing
- Individual component testing (>80% target coverage)
- Mock-based testing for external dependencies
- Property-based testing for data validation

### 10.2 Integration Testing
- End-to-end evaluation pipeline testing
- Cross-language consistency checks
- Guard harness false positive/negative testing

### 10.3 Performance Testing
- Benchmark datasets for regression testing
- Memory usage profiling
- Latency measurements for live runner

### 10.4 Security Testing
- Dependency vulnerability scanning
- Input fuzzing for potential injection points
- Permission and access control verification

## 11. Future Improvements

### 11.1 Short-term (0-3 months)
- Expand dataset size to 100+ examples per language
- Add more African languages (Zulu, Xhosa, Amharic dialects)
- Improve code-switching dataset sophistication
- Add visualization components for results

### 11.2 Medium-term (3-6 months)
- Integration with laya's native evaluation tools
- Export formats for popular ML experiment tracking
- Active learning components for dataset improvement
- Multi-model comparison framework

### 11.3 Long-term (6+ months)
- Community-driven dataset expansion
- Real-time evaluation dashboard
- Integration with AI safety benchmark suites
- Mobile/edge deployment optimizations

## 12. Conclusion

The Laya Africa Evaluation Suite addresses critical gaps in the laya ecosystem by providing:
1. First-of-its-kind African-language evaluation datasets
2. Comprehensive prompt injection security testing
3. Professional evaluation infrastructure for rapid iteration

This suite enables rigorous evaluation of laya's multilingual capabilities while promoting AI safety and inclusivity in natural language processing. The modular, extensible design ensures long-term usefulness as both laya and African language technologies evolve.