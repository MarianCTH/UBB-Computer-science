from src.exceptions.UndoRedoExceptions import *
class UndoRedoService:
    def __init__(self):
        self._operations = []
        self._index = -1
        self._recorded = True

    def recordOperation(self, operation):
        if self.isRecorded():
            if self._operations:
                self._operations[-1].append(operation)
            else:
                self.newOperation()
                self._operations[-1].append(operation)

    def newOperation(self):
        if self.isRecorded() == False:
            return

        self._operations = self._operations[0:self._index + 1]
        self._operations.append([])
        self._index += 1

    def isRecorded(self):
        return self._recorded

    def undo(self):
        if self._index < 0:
            raise UndoException("Too many redo")
            return False

        self._recorded = False

        for oper in self._operations[self._index]:
            oper.undo()

        self._recorded = True

        self._index -= 1
        return True

    def redo(self):
        if self._index + 1 > len(self._operations) - 1:
            raise RedoException("Too many redo")
            return False

        self._recorded = False

        self._index += 1

        for oper in self._operations[self._index]:
            oper.redo()

        self._recorded = True

        return True


class FunctionCall:
    def __init__(self, functionRef, *parameters):
        self._functionRef = functionRef
        self._parameters = parameters

    def call(self):
        self._functionRef(*self._parameters)


class Operation:
    def __init__(self, functionRedo, functionUndo):
        self._functionRedo = functionRedo
        self._functionUndo = functionUndo

    def undo(self):
        self._functionUndo.call()

    def redo(self):
        self._functionRedo.call()