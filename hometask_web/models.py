from django.db import models


# DJANGO MODELS


class Configuration(models.Model):
    title = models.CharField(max_length=50)
    start_at = models.TimeField()
    shutdown_at = models.TimeField()
    allow_internet = models.BooleanField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'configuration'


class PC(models.Model):
    title = models.CharField(max_length=50)
    configuration = models.ManyToManyField(Configuration, through_fields=('pc', 'configuration'), through='ConfigurationPC')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'pc'


class ConfigurationPC(models.Model):
    pc = models.ForeignKey(PC, db_column="pc_id")
    configuration = models.ForeignKey(Configuration, db_column="c_id")

    def __str__(self):
        return "{} {}".format(self.pc.title, self.configuration.title)

    class Meta:
        db_table = 'configuration_pc'


class Adapter(models.Model):
    address = models.CharField(max_length=50)
    pc = models.ForeignKey(PC)

    def __str__(self):
        return "{} {}".format(self.pc.title, self.address)

    class Meta:
        db_table = 'adapter'


class Connection(models.Model):
    from_adapter = models.ForeignKey(Adapter, related_name="from_adapter")
    to_adapter = models.ForeignKey(Adapter, related_name="to_adapter")

    def __str__(self):
        return "{} {}".format(self.from_adapter.address, self.to_adapter.address)

    class Meta:
        db_table = 'connection'
