from breezypythongui import EasyFrame


class TemperatureConverter(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title="Temperature Converter")
        self.addLabel(text="Celsius",
                      row=0, column=0)
        self.celsiusField = self.addFloatField(value=0.0,
                                               row=1,
                                               column=0,
                                               precision=2)

        self.addLabel(text="Fahrenheit",
                      row=0, column=1)
        self.fahrField = self.addFloatField(value=32.0,
                                            row=1,
                                            column=1,
                                            precision=2)

        self.addButton(text=">>>>",
                       row=2, column=0,
                       command=self.computeFahr)
        self.fahrField.bind("<Return>", lambda event: self.computeFahr())
        self.celsiusField.bind("<Return>", lambda event: self.computeCelsius())

        self.addButton(text="<<<<",
                       row=2, column=1,
                       command=self.computeCelsius)
        self.fahrField.bind("<Return>", lambda event: self.computeFahr())
        self.celsiusField.bind("<Return>", lambda event: self.computeCelsius())

    def computeFahr(self):
        degrees = self.celsiusField.getNumber()
        degrees = degrees * 9 / 5 + 32
        self.fahrField.setNumber(degrees)

    def computeCelsius(self):
        degrees = self.fahrField.getNumber()
        degrees = (degrees - 32) * 5 / 9
        self.celsiusField.setNumber(degrees)


def main():
    TemperatureConverter().mainloop()


if __name__ == "__main__":
    main()

