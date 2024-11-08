from abc import abstractmethod

# 1. Design a file compression system where users can select between ZipCompression and RarCompression. Use the Strategy pattern to allow choosing different compression methods.
# Example usage

class CompressionStrategy:
    @abstractmethod
    def compress(self, file: str) -> None:
        pass

class ZipCompression(CompressionStrategy):
    def compress(self, file: str) -> None:
        print(f"Compressing {file} using ZIP")

class RarCompression(CompressionStrategy):
    def compress(self, file: str) -> None:
        print(f"Compressing {file} using RAR")
        
class FileCompressor:
    def __init__(self, compression_strategy: CompressionStrategy):
        self.compression_strategy = compression_strategy
    
    def compress_file(self, file: str) -> None:
        self.compression_strategy.compress(file)
        
compressor = FileCompressor(ZipCompression())
compressor.compress_file("document.txt")

compressor = FileCompressor(RarCompression())
compressor.compress_file("image.jpg")
# The output should be:
# Compressing document.txt using ZIP
# Compressing image.jpg using RAR

# 2. Create a travel planning system where users can choose between CarTravel, BusTravel, and TrainTravel. Implement the Strategy pattern to allow different travel methods with unique messages.
# Example usage
class Travel:
    @abstractmethod
    def plan_trip(self, destination: str) -> None:
        pass

class CarTravel(Travel):
    def plan_trip(self, destination: str) -> None:
        print(f"Traveling to {destination} by Car")

class BusTravel(Travel):
    def plan_trip(self, destination: str) -> None:
        print(f"Traveling to {destination} by Bus")

class TrainTravel(Travel):
    def plan_trip(self, destination: str) -> None:
        print(f"Traveling to {destination} by Train")
        
class TravelContext:
    def __init__(self, travel: Travel):
        self.travel = travel
    
    def plan_trip(self, destination: str) -> None:
        self.travel.plan_trip(destination)

trip = TravelContext(CarTravel())
trip.plan_trip("New York")

trip = TravelContext(TrainTravel())
trip.plan_trip("Boston")

# The output should be:
# Traveling to New York by Car
# Traveling to Boston by Train

# 3. Design a traffic light system with three states: Red, Yellow, and Green. Each state should transition to the next state in a cycle. Implement the State pattern to control the transitions of the traffic light.
# usage
class TrafficLightState:
    @abstractmethod
    def change(self, light: 'TrafficLight') -> None:
        pass
    
class RedState(TrafficLightState):
    def change(self, light: 'TrafficLight') -> None:
        print("Changing from Red to Green.")
        light.state = GreenState()

class GreenState(TrafficLightState):
    def change(self, light: 'TrafficLight') -> None:
        print("Changing from Green to Yellow.")
        light.state = YellowState()

class YellowState(TrafficLightState):
    def change(self, light: 'TrafficLight') -> None:
        print("Changing from Yellow to Red.")
        light.state = RedState()

class TrafficLight:
    def __init__(self):
        self.state = RedState()
        
    def change(self) -> None:
        self.state.change(self)
        
light = TrafficLight()
light.change()  # Red -> Green
light.change()  # Green -> Yellow
light.change()  # Yellow -> Red
# The output should be:
# Changing from Red to Green.
# Changing from Green to Yellow.
# Changing from Yellow to Red.

# 4. Create a document approval process with three states: Draft, Review, and Published. Each state should allow a transition to the next state. Use the State pattern to manage transitions for the document.
# usage

class DocumentState:
    @abstractmethod
    def proceed(self, document: 'Document') -> None:
        pass

class Draft(DocumentState):
    def proceed(self, document: 'Document') -> None:
        print("Document is now under review.")
        document.state = Review()

class Review(DocumentState):
    def proceed(self, document: 'Document') -> None:
        print("Document is now published.")
        document.state = Published()

class Published(DocumentState):
    def proceed(self, document: 'Document') -> None:
        print("Document is already published. No further changes allowed.")
        
class Document:
    def __init__(self):
        self.state = Draft()
        
    def proceed(self) -> None:
        self.state.proceed(self)
        
document = Document()
document.proceed()  # Draft -> Review
document.proceed()  # Review -> Published
document.proceed()  # Published -> No further transition
# The output should be:
# Document is now under review.
# Document is now published.
# Document is already published. No further changes allowed.


