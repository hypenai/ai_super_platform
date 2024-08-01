import numpy as np

def quantize_weights(model):
    for layer in model.layers:
        weights = layer.get_weights()
        quantized_weights = [np.round(w * 256) / 256 for w in weights]
        layer.set_weights(quantized_weights)
    return model

def prune_model(model, pruning_threshold=0.01):
    for layer in model.layers:
        weights = layer.get_weights()
        mask = [np.abs(w) > pruning_threshold for w in weights]
        pruned_weights = [w * m for w, m in zip(weights, mask)]
        layer.set_weights(pruned_weights)
    return model

print("Model compression techniques ready for deployment.")
