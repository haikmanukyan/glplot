class AnimatedAttr:
    def get_shape(self, arr):
        shape = []
        while hasattr(arr, '__len__'):
            shape.append(len(arr))
            arr = arr[0]
        return shape

    def __init__(self, figure, value, dims = 1):
        self.figure = figure
        self.dims = dims
        self.value = value
    
    def __len__(self):
        return len(self())
    
    def __call__(self):
        if callable(self.value): return self.value()
        if len(self.get_shape(self.value)) == self.dims:
            return self.value
        else:
            return self.value[self.figure.frame_idx % len(self.value)]