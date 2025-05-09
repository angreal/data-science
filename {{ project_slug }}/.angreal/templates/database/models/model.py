{% raw %}
"""
{{ model_name_title }} model.
"""

from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Float, DateTime
from sqlalchemy.orm import relationship
from .base import BaseModel


class {{ model_name }}(BaseModel):
    """
    {{ model_description }}
    """
    __tablename__ = '{{ table_name }}'
    
    # Define your columns here:
    # name = Column(String, nullable=False)
    # description = Column(String)
    
    # Define relationships here (if needed):
    # items = relationship("{{ RelatedModel }}", back_populates="{{ related_attribute }}")
    
    def __repr__(self):
        return f"<{{ model_name }}(id={self.id})>"
{% endraw %} 