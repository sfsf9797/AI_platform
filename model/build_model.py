import onnxruntime as ort
import numpy as np

class OnnxModel():

    def __init__(self, modelPath = './model/model_path/model.onnx') -> None:
        self.modelPath = modelPath
        self.ort_session = ort.InferenceSession(self.modelPath)

    def inference(self, img: np.ndarray, window: int) -> np.array:

        '''
        make prediction by model

        parameters
        ----------
        img:
         input image
        window:
            window size of image
        
        Returns
        ----------
        output image's array
        '''

        img = img.reshape(1,3,window,window)
        
        output = self.ort_session.run(
            None,
            {"input.1": img.astype(np.float32)},

        )

        return np.array(output).reshape(window,window)

